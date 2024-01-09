"""Adding initial tables and seed tables with data

Revision ID: 4c712d84d5c4
Revises:
Create Date: 2024-01-06 21:10:20.798818

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel
import uuid


# revision identifiers, used by Alembic.
revision = '4c712d84d5c4'
down_revision = None
branch_labels = None
depends_on = None

# Generate a random UUID
ISSF10ARF_uuid = uuid.uuid4()
ISSF10APF_uuid = uuid.uuid4()

countries = [
    ('AF', 'Afghanistan', str(uuid.uuid4())),
    ('AL', 'Albania', str(uuid.uuid4())),
    ('AM', 'Armenia', str(uuid.uuid4())),
    ('AR', 'Argentina', str(uuid.uuid4())),
    ('AT', 'Austria', str(uuid.uuid4())),
    ('AU', 'Australia', str(uuid.uuid4())),
    ('AZ', 'Azerbaijan', str(uuid.uuid4())),
    ('BA', 'Bosnia and Herzegovina', str(uuid.uuid4())),
    ('BD', 'Bangladesh', str(uuid.uuid4())),
    ('BE', 'Belgium', str(uuid.uuid4())),
    ('BH', 'Bahrain', str(uuid.uuid4())),
    ('BN', 'Brunei', str(uuid.uuid4())),
    ('BR', 'Brazil', str(uuid.uuid4())),
    ('BT', 'Bhutan', str(uuid.uuid4())),
    ('BY', 'Belarus', str(uuid.uuid4())),
    ('CA', 'Canada', str(uuid.uuid4())),
    ('CH', 'Switzerland', str(uuid.uuid4())),
    ('CL', 'Chile', str(uuid.uuid4())),
    ('CN', 'China', str(uuid.uuid4())),
    ('CO', 'Colombia', str(uuid.uuid4())),
    ('CY', 'Cyprus', str(uuid.uuid4())),
    ('CZ', 'Czech Republic', str(uuid.uuid4())),
    ('DE', 'Germany', str(uuid.uuid4())),
    ('DK', 'Denmark', str(uuid.uuid4())),
    ('EC', 'Ecuador', str(uuid.uuid4())),
    ('EE', 'Estonia', str(uuid.uuid4())),
    ('EG', 'Egypt', str(uuid.uuid4())),
    ('ES', 'Spain', str(uuid.uuid4())),
    ('FI', 'Finland', str(uuid.uuid4())),
    ('FJ', 'Fiji', str(uuid.uuid4())),
    ('FM', 'Micronesia', str(uuid.uuid4())),
    ('FR', 'France', str(uuid.uuid4())),
    ('GE', 'Georgia', str(uuid.uuid4())),
    ('GY', 'Guyana', str(uuid.uuid4())),
    ('ID', 'Indonesia', str(uuid.uuid4())),
    ('IE', 'Ireland', str(uuid.uuid4())),
    ('IL', 'Israel', str(uuid.uuid4())),
    ('IN', 'India', str(uuid.uuid4())),
    ('IQ', 'Iraq', str(uuid.uuid4())),
    ('IR', 'Iran', str(uuid.uuid4())),
    ('IS', 'Iceland', str(uuid.uuid4())),
    ('IT', 'Italy', str(uuid.uuid4())),
    ('JO', 'Jordan', str(uuid.uuid4())),
    ('JP', 'Japan', str(uuid.uuid4())),
    ('KG', 'Kyrgyzstan', str(uuid.uuid4())),
    ('KH', 'Cambodia', str(uuid.uuid4())),
    ('KI', 'Kiribati', str(uuid.uuid4())),
    ('KW', 'Kuwait', str(uuid.uuid4())),
    ('KZ', 'Kazakhstan', str(uuid.uuid4())),
    ('LA', 'Laos', str(uuid.uuid4())),
    ('LB', 'Lebanon', str(uuid.uuid4())),
    ('LI', 'Liechtenstein', str(uuid.uuid4())),
    ('LK', 'Sri Lanka', str(uuid.uuid4())),
    ('LT', 'Lithuania', str(uuid.uuid4())),
    ('LU', 'Luxembourg', str(uuid.uuid4())),
    ('LV', 'Latvia', str(uuid.uuid4())),
    ('MA', 'Morocco', str(uuid.uuid4())),
    ('MC', 'Monaco', str(uuid.uuid4())),
    ('MD', 'Moldova', str(uuid.uuid4())),
    ('ME', 'Montenegro', str(uuid.uuid4())),
    ('MK', 'North Macedonia', str(uuid.uuid4())),
    ('MN', 'Mongolia', str(uuid.uuid4())),
    ('MR', 'Mauritania', str(uuid.uuid4())),
    ('MT', 'Malta', str(uuid.uuid4())),
    ('MV', 'Maldives', str(uuid.uuid4())),
    ('MX', 'Mexico', str(uuid.uuid4())),
    ('MY', 'Malaysia', str(uuid.uuid4())),
    ('NA', 'Namibia', str(uuid.uuid4())),
    ('NG', 'Nigeria', str(uuid.uuid4())),
    ('NI', 'Nicaragua', str(uuid.uuid4())),
    ('NL', 'Netherlands', str(uuid.uuid4())),
    ('NO', 'Norway', str(uuid.uuid4())),
    ('NP', 'Nepal', str(uuid.uuid4())),
    ('NR', 'Nauru', str(uuid.uuid4())),
    ('NZ', 'New Zealand', str(uuid.uuid4())),
    ('OM', 'Oman', str(uuid.uuid4())),
    ('PA', 'Panama', str(uuid.uuid4())),
    ('PE', 'Peru', str(uuid.uuid4())),
    ('PH', 'Philippines', str(uuid.uuid4())),
    ('PK', 'Pakistan', str(uuid.uuid4())),
    ('PL', 'Poland', str(uuid.uuid4())),
    ('PS', 'Palestine', str(uuid.uuid4())),
    ('PT', 'Portugal', str(uuid.uuid4())),
    ('PY', 'Paraguay', str(uuid.uuid4())),
    ('QA', 'Qatar', str(uuid.uuid4())),
    ('RO', 'Romania', str(uuid.uuid4())),
    ('RS', 'Serbia', str(uuid.uuid4())),
    ('RU', 'Russia', str(uuid.uuid4())),
    ('RW', 'Rwanda', str(uuid.uuid4())),
    ('SA', 'Saudi Arabia', str(uuid.uuid4())),
    ('SB', 'Solomon Islands', str(uuid.uuid4())),
    ('SC', 'Seychelles', str(uuid.uuid4())),
    ('SE', 'Sweden', str(uuid.uuid4())),
    ('SG', 'Singapore', str(uuid.uuid4())),
    ('SI', 'Slovenia', str(uuid.uuid4())),
    ('SK', 'Slovakia', str(uuid.uuid4())),
    ('SR', 'Suriname', str(uuid.uuid4())),
    ('ST', 'Sao Tome and Principe', str(uuid.uuid4())),
    ('SV', 'El Salvador', str(uuid.uuid4())),
    ('SY', 'Syria', str(uuid.uuid4())),
    ('SZ', 'Eswatini', str(uuid.uuid4())),
    ('TH', 'Thailand', str(uuid.uuid4())),
    ('TJ', 'Tajikistan', str(uuid.uuid4())),
    ('TL', 'Timor-Leste', str(uuid.uuid4())),
    ('TO', 'Tonga', str(uuid.uuid4())),
    ('TR', 'Turkey', str(uuid.uuid4())),
    ('TT', 'Trinidad and Tobago', str(uuid.uuid4())),
    ('TV', 'Tuvalu', str(uuid.uuid4())),
    ('TW', 'Taiwan', str(uuid.uuid4())),
    ('TZ', 'Tanzania', str(uuid.uuid4())),
    ('UA', 'Ukraine', str(uuid.uuid4())),
    ('UG', 'Uganda', str(uuid.uuid4())),
    ('US', 'United States', str(uuid.uuid4())),
    ('UY', 'Uruguay', str(uuid.uuid4())),
    ('UZ', 'Uzbekistan', str(uuid.uuid4())),
    ('VC', 'Saint Vincent and the Grenadines', str(uuid.uuid4())),
    ('VE', 'Venezuela', str(uuid.uuid4())),
    ('VN', 'Vietnam', str(uuid.uuid4())),
    ('VU', 'Vanuatu', str(uuid.uuid4())),
    ('WS', 'Samoa', str(uuid.uuid4())),
    ('YE', 'Yemen', str(uuid.uuid4())),
    ('ZA', 'South Africa', str(uuid.uuid4())),
    ('ZM', 'Zambia', str(uuid.uuid4())),
    ('ZW', 'Zimbabwe', str(uuid.uuid4())),
    ('XK', 'Kosovo', str(uuid.uuid4())),
]

range_manufactor = [
    ('Megalink', str(uuid.uuid4())),
    ('SIUS', str(uuid.uuid4())),
]

discipline = [
    ('ISSF 10m AR Final', 'ISSF10ARF', 'ENABLED', f'{ISSF10ARF_uuid}'),
    ('ISSF 10m AP Final', 'ISSF10APF', 'ENABLED', f'{ISSF10APF_uuid}'),
]

discipline_series = [
    (1, 'Sighters', 'SIGHT', 300, 'NULL', 'NULL', 'NULL', 'NULL', f'{uuid.uuid4()}', f'{ISSF10ARF_uuid}'),
    (2, '1-5', 'MATCH', 250, 5, False, False, 'NULL', f'{uuid.uuid4()}', f'{ISSF10ARF_uuid}'),
    (3, '6-10', 'MATCH', 250, 5, False, False, 'NULL', f'{uuid.uuid4()}', f'{ISSF10ARF_uuid}'),
    (4, '11-12', 'MATCH', 50, 2, True, True, 1, f'{uuid.uuid4()}', f'{ISSF10ARF_uuid}'),
    (5, '13-14', 'MATCH', 50, 2, True, True, 1, f'{uuid.uuid4()}', f'{ISSF10ARF_uuid}'),
    (6, '15-16', 'MATCH', 50, 2, True, True, 1, f'{uuid.uuid4()}', f'{ISSF10ARF_uuid}'),
    (7, '17-18', 'MATCH', 50, 2, True, True, 1, f'{uuid.uuid4()}', f'{ISSF10ARF_uuid}'),
    (8, '19-20', 'MATCH', 50, 2, True, True, 1, f'{uuid.uuid4()}', f'{ISSF10ARF_uuid}'),
    (9, '21-22', 'MATCH', 50, 2, True, True, 1, f'{uuid.uuid4()}', f'{ISSF10ARF_uuid}'),
    (10, '23-24', 'MATCH', 50, 2, True, True, 1, f'{uuid.uuid4()}', f'{ISSF10ARF_uuid}'),
]


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('country',
    sa.Column('code', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('id', sqlmodel.sql.sqltypes.GUID(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    schema='rcb'
    )
    op.create_index(op.f('ix_rcb_country_id'), 'country', ['id'], unique=False, schema='rcb')
    op.create_table('discipline',
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('shortname', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('status', sa.Enum('DISABLED', 'TESTING', 'ENABLED', name='disciplinestatus'), nullable=False),
    sa.Column('id', sqlmodel.sql.sqltypes.GUID(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    schema='rcb'
    )
    op.create_index(op.f('ix_rcb_discipline_id'), 'discipline', ['id'], unique=False, schema='rcb')
    op.create_table('range_manufactor',
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('id', sqlmodel.sql.sqltypes.GUID(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    schema='rcb'
    )
    op.create_index(op.f('ix_rcb_range_manufactor_id'), 'range_manufactor', ['id'], unique=False, schema='rcb')
    op.create_table('competition',
    sa.Column('event', sqlmodel.sql.sqltypes.GUID(), nullable=False),
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('shortname', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('startdate', sa.DateTime, nullable=False),
    sa.Column('enddate', sa.DateTime, nullable=True),
    sa.Column('status', sa.Enum('DISABLED', 'TESTING', 'ENABLED', name='competitionstatus'), nullable=False),
    sa.Column('id', sqlmodel.sql.sqltypes.GUID(), nullable=False),
    sa.Column('discipline_id', sqlmodel.sql.sqltypes.GUID(), nullable=False),
    sa.ForeignKeyConstraint(['discipline_id'], ['rcb.discipline.id'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='rcb'
    )
    op.create_index(op.f('ix_rcb_competition_id'), 'competition', ['id'], unique=False, schema='rcb')
    op.create_table('discipline_series',
    sa.Column('series', sa.Integer(), nullable=False),
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('type', sa.Enum('SIGHT', 'MATCH', 'SHOOTOFF', name='seriestype'), nullable=False),
    sa.Column('time', sa.Integer(), nullable=False),
    sa.Column('number_of_shots', sa.Integer(), nullable=True),
    sa.Column('single_shots', sa.Boolean(), nullable=True),
    sa.Column('elimination', sa.Boolean(), nullable=True),
    sa.Column('shooters_to_eliminate', sa.Integer(), nullable=True),
    sa.Column('id', sqlmodel.sql.sqltypes.GUID(), nullable=False),
    sa.Column('discipline_id', sqlmodel.sql.sqltypes.GUID(), nullable=False),
    sa.ForeignKeyConstraint(['discipline_id'], ['rcb.discipline.id'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='rcb'
    )
    op.create_index(op.f('ix_rcb_discipline_series_id'), 'discipline_series', ['id'], unique=False, schema='rcb')
    op.create_table('shooting_club',
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('shortname', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('id', sqlmodel.sql.sqltypes.GUID(), nullable=False),
    sa.Column('country_id', sqlmodel.sql.sqltypes.GUID(), nullable=False),
    sa.ForeignKeyConstraint(['country_id'], ['rcb.country.id'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='rcb'
    )
    op.create_index(op.f('ix_rcb_shooting_club_id'), 'shooting_club', ['id'], unique=False, schema='rcb')
    op.create_table('event',
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('startdate', sa.DateTime, nullable=False),
    sa.Column('enddate', sa.DateTime, nullable=True),
    sa.Column('status', sa.Enum('CANCELLED', 'FINISHED', 'PLANNED', 'STARTED', name='eventstatus'), nullable=False),
    sa.Column('id', sqlmodel.sql.sqltypes.GUID(), nullable=False),
    sa.Column('shooting_club_id', sqlmodel.sql.sqltypes.GUID(), nullable=False),
    sa.ForeignKeyConstraint(['shooting_club_id'], ['rcb.shooting_club.id'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='rcb'
    )
    op.create_index(op.f('ix_rcb_event_id'), 'event', ['id'], unique=False, schema='rcb')
    op.create_table('shooting_range',
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('lanes', sa.Integer(), nullable=False),
    sa.Column('first_lane', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('id', sqlmodel.sql.sqltypes.GUID(), nullable=False),
    sa.Column('shooting_club_id', sqlmodel.sql.sqltypes.GUID(), nullable=False),
    sa.Column('range_manufactor_id', sqlmodel.sql.sqltypes.GUID(), nullable=False),
    sa.ForeignKeyConstraint(['range_manufactor_id'], ['rcb.range_manufactor.id'], ),
    sa.ForeignKeyConstraint(['shooting_club_id'], ['rcb.shooting_club.id'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='rcb'
    )
    op.create_index(op.f('ix_rcb_shooting_range_id'), 'shooting_range', ['id'], unique=False, schema='rcb')
    op.create_table('event_range_link',
    sa.Column('event_id', sqlmodel.sql.sqltypes.GUID(), nullable=False),
    sa.Column('shooting_range_id', sqlmodel.sql.sqltypes.GUID(), nullable=False),
    sa.ForeignKeyConstraint(['event_id'], ['rcb.event.id'], ),
    sa.ForeignKeyConstraint(['shooting_range_id'], ['rcb.shooting_range.id'], ),
    sa.PrimaryKeyConstraint('event_id', 'shooting_range_id'),
    schema='rcb'
    )
    for data in countries:
        op.execute(
            f"INSERT INTO country (code, name, id) VALUES "
            f"('{data[0]}', '{data[1]}', '{data[2]}')"
        )
    for data in range_manufactor:
        op.execute(
            f"INSERT INTO range_manufactor (name, id) VALUES "
            f"('{data[0]}', '{data[1]}')"
        )
    for data in discipline:
        op.execute(
            f"INSERT INTO discipline (name, shortname, status, id) VALUES "
            f"('{data[0]}', '{data[1]}', '{data[2]}', '{data[3]}')"
        )
    for data in discipline_series:
        op.execute(
            f"INSERT INTO discipline_series (series, name, type, time, number_of_shots, single_shots, elimination, shooters_to_eliminate, id, discipline_id) VALUES "
            f"({data[0]}, '{data[1]}', '{data[2]}', {data[3]}, {data[4]}, {data[5]}, {data[6]}, {data[7]}, '{data[8]}', '{data[9]}')"
        )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('event_range_link', schema='rcb')
    op.drop_index(op.f('ix_rcb_shooting_range_id'), table_name='shooting_range', schema='rcb')
    op.drop_table('shooting_range', schema='rcb')
    op.drop_index(op.f('ix_rcb_event_id'), table_name='event', schema='rcb')
    op.drop_table('event', schema='rcb')
    op.drop_index(op.f('ix_rcb_shooting_club_id'), table_name='shooting_club', schema='rcb')
    op.drop_table('shooting_club', schema='rcb')
    op.drop_index(op.f('ix_rcb_discipline_series_id'), table_name='discipline_series', schema='rcb')
    op.drop_table('discipline_series', schema='rcb')
    op.drop_index(op.f('ix_rcb_competition_id'), table_name='competition', schema='rcb')
    op.drop_table('competition', schema='rcb')
    op.drop_index(op.f('ix_rcb_range_manufactor_id'), table_name='range_manufactor', schema='rcb')
    op.drop_table('range_manufactor', schema='rcb')
    op.drop_index(op.f('ix_rcb_discipline_id'), table_name='discipline', schema='rcb')
    op.drop_table('discipline', schema='rcb')
    op.drop_index(op.f('ix_rcb_country_id'), table_name='country', schema='rcb')
    op.drop_table('country', schema='rcb')
    # ### end Alembic commands ###