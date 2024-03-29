"""Adding data for development environment

Revision ID: eb0bee64c83f
Revises: af9eb26ee078
Create Date: 2024-01-07 16:19:36.094983

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import text
import sqlmodel
import uuid

# revision identifiers, used by Alembic.
revision = 'eb0bee64c83f'
down_revision = '4c712d84d5c4'
branch_labels = None
depends_on = None


# Generate a random UUID
event_1_uuid = uuid.uuid4()
event_2_uuid = uuid.uuid4()

shooting_club = [
    ('Viborg Skytteforening', 'VSF', str(uuid.uuid4()), 'DK'),
    ('Aarhus Riffel Klub', 'ÅRK', str(uuid.uuid4()), 'DK'),
]

shooting_range = [
    ('10m', 10, '1', 'EBA2ED57-BF56-47DE-91F8-DEA032843FE3', 'Viborg Skytteforening', 'Megalink'),
    ('10m', 10, '1', str(uuid.uuid4()), 'Aarhus Riffel Klub', 'SIUS'),
]

event = [
    ('Viborg Open Air', '2024-01-08T14:30:00', 'PLANNED', str(event_1_uuid), 'Viborg Skytteforening'),
    ('Denmark Open Air', '2024-02-08T14:30:00', 'PLANNED', str(event_2_uuid), 'Aarhus Riffel Klub'),
]

competition = [
    (str(event_1_uuid), '10m AR Final - Men', '10M_AR_FINAL_M', '2024-01-09T16:30:00', 'PLANNED', str(uuid.uuid4()), 'ISSF_10M_AR_FINAL', 'EBA2ED57-BF56-47DE-91F8-DEA032843FE3'),
    (str(event_1_uuid), '10m AR Final - Women', '10M_AR_FINAL_W', '2024-01-09T18:00:00', 'PLANNED', str(uuid.uuid4()), 'ISSF_10M_AR_FINAL', 'EBA2ED57-BF56-47DE-91F8-DEA032843FE3'),
]


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###

    for data in shooting_club:
        # Retrieve the ID for the country
        country_id = op.get_bind().execute(text(
            f"SELECT id FROM country WHERE code = '{data[3]}'"
        )).scalar()

        op.execute(
            f"INSERT INTO shooting_club (name, shortname, id, country_id) VALUES "
            f"('{data[0]}', '{data[1]}', '{data[2]}', '{country_id}')"
        )
    
    for data in shooting_range:
        # Retrieve the ID for the shooting_club
        shooting_club_id = op.get_bind().execute(text(
            f"SELECT id FROM shooting_club WHERE name = '{data[4]}'"
        )).scalar()

        shooting_club_id = shooting_club_id if shooting_club_id is not None else None

        range_manufactor_id = op.get_bind().execute(text(
            f"SELECT id FROM range_manufactor WHERE name = '{data[5]}'"
        )).scalar()

        range_manufactor_id = range_manufactor_id if range_manufactor_id is not None else None

        op.execute(
            f"INSERT INTO shooting_range (name, lanes, first_lane, id, shooting_club_id, range_manufactor_id) VALUES "
            f"('{data[0]}', {data[1]}, '{data[2]}', '{data[3]}', '{shooting_club_id}', '{range_manufactor_id}')"
        )

    for data in event:
        # Retrieve the ID for the shooting_club
        shooting_club_id = op.get_bind().execute(text(
            f"SELECT id FROM shooting_club WHERE name = '{data[4]}'"
        )).scalar()

        op.execute(
            f"INSERT INTO event (name, startdate, status, id, shooting_club_id) VALUES "
            f"('{data[0]}', '{data[1]}', '{data[2]}', '{data[3]}', '{shooting_club_id}')"
        )

    for data in competition:
        # Retrieve the ID for the discipline
        discipline_id = op.get_bind().execute(text(
            f"SELECT id FROM discipline WHERE shortname = '{data[6]}'"
        )).scalar()

        op.execute(
            f"INSERT INTO competition (event_id, name, shortname, startdate, status, id, discipline_id, shooting_range_id) VALUES "
            f"('{data[0]}', '{data[1]}', '{data[2]}', '{data[3]}', '{data[4]}', '{data[5]}', '{discipline_id}', '{data[7]}')"
        )

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###