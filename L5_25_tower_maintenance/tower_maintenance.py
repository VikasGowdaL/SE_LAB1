
"""Track tower maintenance records and assess maintenance risks."""

import sqlite3

conn = sqlite3.connect(":memory:")


def initialize_database():
    """Create the database table for tower records."""
    conn.execute(
        """
        CREATE TABLE towers (
            id INTEGER PRIMARY KEY,
            site TEXT,
            last_service INTEGER,
            faults INTEGER
        )
        """
    )


def add_tower(site, last_service, faults=0):
    """Add a tower record to the database."""
    conn.execute(
        """
        INSERT INTO towers (site, last_service, faults)
        VALUES (?, ?, ?)
        """,
        (site, last_service, faults),
    )
    conn.commit()


def service_tower(tower_id, year):
    """Service a tower and reset its fault count."""
    cursor = conn.execute(
        """
        UPDATE towers
        SET last_service = ?, faults = 0
        WHERE id = ?
        """,
        (year, tower_id),
    )
    conn.commit()
    return cursor.rowcount > 0


def overdue(year):
    """Return sites whose last service was at least two years ago."""
    rows = conn.execute(
        "SELECT site, last_service FROM towers"
    ).fetchall()

    return [
        site
        for site, last_service in rows
        if year - last_service >= 2
    ]


def risk_level(tower_id):
    """Return the risk level based on a tower's fault count."""
    row = conn.execute(
        "SELECT faults FROM towers WHERE id = ?",
        (tower_id,),
    ).fetchone()

    if row is None:
        return "unknown"
    if row[0] > 3:
        return "high"
    return "normal"


def snapshot():
    """Return all tower records as a list of tuples."""
    return conn.execute("SELECT * FROM towers").fetchall()


def main():
    """Run the tower maintenance demonstration."""
    initialize_database()
    add_tower("Ridge-A", 2021, 5)
    add_tower("Coast-B", 2024)

    service_count = 0
    if service_tower(2, 2025):
        service_count += 1

    total = len(snapshot())
    print(overdue(2025), risk_level(1), total, service_count)


if __name__ == "__main__":
    main()
