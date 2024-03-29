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
    ('AD', 'Andorra', str(uuid.uuid4())),
    ('AE', 'United Arab Emirates', str(uuid.uuid4())),
    ('AF', 'Afghanistan', str(uuid.uuid4())),
    ('AG', 'Antigua and Barbuda', str(uuid.uuid4())),
    ('AL', 'Albania', str(uuid.uuid4())),
    ('AM', 'Armenia', str(uuid.uuid4())),
    ('AO', 'Angola', str(uuid.uuid4())),
    ('AR', 'Argentina', str(uuid.uuid4())),
    ('AT', 'Austria', str(uuid.uuid4())),
    ('AU', 'Australia', str(uuid.uuid4())),
    ('AZ', 'Azerbaijan', str(uuid.uuid4())),
    ('BA', 'Bosnia and Herzegovina', str(uuid.uuid4())),
    ('BB', 'Barbados', str(uuid.uuid4())),
    ('BD', 'Bangladesh', str(uuid.uuid4())),
    ('BE', 'Belgium', str(uuid.uuid4())),
    ('BF', 'Burkina Faso', str(uuid.uuid4())),
    ('BG', 'Bulgaria', str(uuid.uuid4())),
    ('BH', 'Bahrain', str(uuid.uuid4())),
    ('BI', 'Burundi', str(uuid.uuid4())),
    ('BJ', 'Benin', str(uuid.uuid4())),
    ('BN', 'Brunei', str(uuid.uuid4())),
    ('BO', 'Bolivia', str(uuid.uuid4())),
    ('BR', 'Brazil', str(uuid.uuid4())),
    ('BS', 'Bahamas', str(uuid.uuid4())),
    ('BT', 'Bhutan', str(uuid.uuid4())),
    ('BW', 'Botswana', str(uuid.uuid4())),
    ('BY', 'Belarus', str(uuid.uuid4())),
    ('BZ', 'Belize', str(uuid.uuid4())),
    ('CA', 'Canada', str(uuid.uuid4())),
    ('CD', 'Democratic Republic of the Congo', str(uuid.uuid4())),
    ('CF', 'Central African Republic', str(uuid.uuid4())),
    ('CG', 'Republic of the Congo', str(uuid.uuid4())),
    ('CH', 'Switzerland', str(uuid.uuid4())),
    ('CI', 'Ivory Coast', str(uuid.uuid4())),
    ('CL', 'Chile', str(uuid.uuid4())),
    ('CM', 'Cameroon', str(uuid.uuid4())),
    ('CN', 'China', str(uuid.uuid4())),
    ('CO', 'Colombia', str(uuid.uuid4())),
    ('CR', 'Costa Rica', str(uuid.uuid4())),
    ('CU', 'Cuba', str(uuid.uuid4())),
    ('CY', 'Cyprus', str(uuid.uuid4())),
    ('CZ', 'Czech Republic', str(uuid.uuid4())),
    ('DE', 'Germany', str(uuid.uuid4())),
    ('DJ', 'Djibouti', str(uuid.uuid4())),
    ('DK', 'Denmark', str(uuid.uuid4())),
    ('DM', 'Dominica', str(uuid.uuid4())),
    ('DO', 'Dominican Republic', str(uuid.uuid4())),
    ('DZ', 'Algeria', str(uuid.uuid4())),
    ('EC', 'Ecuador', str(uuid.uuid4())),
    ('EE', 'Estonia', str(uuid.uuid4())),
    ('EG', 'Egypt', str(uuid.uuid4())),
    ('EH', 'Western Sahara', str(uuid.uuid4())),
    ('ER', 'Eritrea', str(uuid.uuid4())),
    ('ES', 'Spain', str(uuid.uuid4())),
    ('ET', 'Ethiopia', str(uuid.uuid4())),
    ('FI', 'Finland', str(uuid.uuid4())),
    ('FJ', 'Fiji', str(uuid.uuid4())),
    ('FM', 'Micronesia', str(uuid.uuid4())),
    ('FR', 'France', str(uuid.uuid4())),
    ('GA', 'Gabon', str(uuid.uuid4())),
    ('GB', 'United Kingdom', str(uuid.uuid4())),
    ('GD', 'Grenada', str(uuid.uuid4())),
    ('GE', 'Georgia', str(uuid.uuid4())),
    ('GH', 'Ghana', str(uuid.uuid4())),
    ('GM', 'Gambia', str(uuid.uuid4())),
    ('GN', 'Guinea', str(uuid.uuid4())),
    ('GQ', 'Equatorial Guinea', str(uuid.uuid4())),
    ('GR', 'Greece', str(uuid.uuid4())),
    ('GT', 'Guatemala', str(uuid.uuid4())),
    ('GW', 'Guinea-Bissau', str(uuid.uuid4())),
    ('GY', 'Guyana', str(uuid.uuid4())),
    ('HN', 'Honduras', str(uuid.uuid4())),
    ('HR', 'Croatia', str(uuid.uuid4())),
    ('HT', 'Haiti', str(uuid.uuid4())),
    ('HU', 'Hungary', str(uuid.uuid4())),
    ('ID', 'Indonesia', str(uuid.uuid4())),
    ('IE', 'Ireland', str(uuid.uuid4())),
    ('IL', 'Israel', str(uuid.uuid4())),
    ('IN', 'India', str(uuid.uuid4())),
    ('IQ', 'Iraq', str(uuid.uuid4())),
    ('IR', 'Iran', str(uuid.uuid4())),
    ('IS', 'Iceland', str(uuid.uuid4())),
    ('IT', 'Italy', str(uuid.uuid4())),
    ('JM', 'Jamaica', str(uuid.uuid4())),
    ('JO', 'Jordan', str(uuid.uuid4())),
    ('JP', 'Japan', str(uuid.uuid4())),
    ('KE', 'Kenya', str(uuid.uuid4())),
    ('KG', 'Kyrgyzstan', str(uuid.uuid4())),
    ('KH', 'Cambodia', str(uuid.uuid4())),
    ('KI', 'Kiribati', str(uuid.uuid4())),
    ('KM', 'Comoros', str(uuid.uuid4())),
    ('KN', 'Saint Kitts and Nevis', str(uuid.uuid4())),
    ('KP', 'North Korea', str(uuid.uuid4())),
    ('KR', 'South Korea', str(uuid.uuid4())),
    ('KW', 'Kuwait', str(uuid.uuid4())),
    ('KZ', 'Kazakhstan', str(uuid.uuid4())),
    ('LA', 'Laos', str(uuid.uuid4())),
    ('LB', 'Lebanon', str(uuid.uuid4())),
    ('LC', 'Saint Lucia', str(uuid.uuid4())),
    ('LI', 'Liechtenstein', str(uuid.uuid4())),
    ('LK', 'Sri Lanka', str(uuid.uuid4())),
    ('LR', 'Liberia', str(uuid.uuid4())),
    ('LS', 'Lesotho', str(uuid.uuid4())),
    ('LT', 'Lithuania', str(uuid.uuid4())),
    ('LU', 'Luxembourg', str(uuid.uuid4())),
    ('LV', 'Latvia', str(uuid.uuid4())),
    ('LY', 'Libya', str(uuid.uuid4())),
    ('MA', 'Morocco', str(uuid.uuid4())),
    ('MC', 'Monaco', str(uuid.uuid4())),
    ('MD', 'Moldova', str(uuid.uuid4())),
    ('ME', 'Montenegro', str(uuid.uuid4())),
    ('MG', 'Madagascar', str(uuid.uuid4())),
    ('MH', 'Marshall Islands', str(uuid.uuid4())),
    ('MK', 'North Macedonia', str(uuid.uuid4())),
    ('ML', 'Mali', str(uuid.uuid4())),
    ('MM', 'Myanmar', str(uuid.uuid4())),
    ('MN', 'Mongolia', str(uuid.uuid4())),
    ('MR', 'Mauritania', str(uuid.uuid4())),
    ('MT', 'Malta', str(uuid.uuid4())),
    ('MU', 'Mauritius', str(uuid.uuid4())),
    ('MV', 'Maldives', str(uuid.uuid4())),
    ('MW', 'Malawi', str(uuid.uuid4())),
    ('MX', 'Mexico', str(uuid.uuid4())),
    ('MY', 'Malaysia', str(uuid.uuid4())),
    ('MZ', 'Mozambique', str(uuid.uuid4())),
    ('NA', 'Namibia', str(uuid.uuid4())),
    ('NE', 'Niger', str(uuid.uuid4())),
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
    ('PG', 'Papua New Guinea', str(uuid.uuid4())),
    ('PH', 'Philippines', str(uuid.uuid4())),
    ('PK', 'Pakistan', str(uuid.uuid4())),
    ('PL', 'Poland', str(uuid.uuid4())),
    ('PS', 'Palestine', str(uuid.uuid4())),
    ('PT', 'Portugal', str(uuid.uuid4())),
    ('PW', 'Palau', str(uuid.uuid4())),
    ('PY', 'Paraguay', str(uuid.uuid4())),
    ('QA', 'Qatar', str(uuid.uuid4())),
    ('RO', 'Romania', str(uuid.uuid4())),
    ('RS', 'Serbia', str(uuid.uuid4())),
    ('RU', 'Russia', str(uuid.uuid4())),
    ('RW', 'Rwanda', str(uuid.uuid4())),
    ('SA', 'Saudi Arabia', str(uuid.uuid4())),
    ('SB', 'Solomon Islands', str(uuid.uuid4())),
    ('SC', 'Seychelles', str(uuid.uuid4())),
    ('SD', 'Sudan', str(uuid.uuid4())),
    ('SE', 'Sweden', str(uuid.uuid4())),
    ('SG', 'Singapore', str(uuid.uuid4())),
    ('SI', 'Slovenia', str(uuid.uuid4())),
    ('SK', 'Slovakia', str(uuid.uuid4())),
    ('SL', 'Sierra Leone', str(uuid.uuid4())),
    ('SM', 'San Marino', str(uuid.uuid4())),
    ('SN', 'Senegal', str(uuid.uuid4())),
    ('SO', 'Somalia', str(uuid.uuid4())),
    ('SR', 'Suriname', str(uuid.uuid4())),
    ('SS', 'South Sudan', str(uuid.uuid4())),
    ('ST', 'Sao Tome and Principe', str(uuid.uuid4())),
    ('SV', 'El Salvador', str(uuid.uuid4())),
    ('SY', 'Syria', str(uuid.uuid4())),
    ('SZ', 'Eswatini', str(uuid.uuid4())),
    ('TD', 'Chad', str(uuid.uuid4())),
    ('TG', 'Togo', str(uuid.uuid4())),
    ('TH', 'Thailand', str(uuid.uuid4())),
    ('TJ', 'Tajikistan', str(uuid.uuid4())),
    ('TL', 'Timor-Leste', str(uuid.uuid4())),
    ('TN', 'Tunisia', str(uuid.uuid4())),
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
    ('XK', 'Kosovo', str(uuid.uuid4())),
    ('YE', 'Yemen', str(uuid.uuid4())),
    ('ZA', 'South Africa', str(uuid.uuid4())),
    ('ZM', 'Zambia', str(uuid.uuid4())),
    ('ZW', 'Zimbabwe', str(uuid.uuid4())),
]

range_manufactor = [
    ('Megalink', str(uuid.uuid4())),
    ('SIUS', str(uuid.uuid4())),
]

discipline = [
    ('ISSF 10m AR Final', 'ISSF_10M_AR_FINAL', 'ENABLED', f'{ISSF10ARF_uuid}'),
    ('ISSF 10m AP Final', 'ISSF_10M_AP_FINAL', 'ENABLED', f'{ISSF10APF_uuid}'),
]

discipline_series = [
    (1, 'Sighters', 'SIGHT', 300, 'NULL', 'NULL', 'NULL', 'NULL', str(uuid.uuid4()), f'{ISSF10ARF_uuid}'),
    (2, '1-5', 'MATCH', 250, 5, False, False, 'NULL', str(uuid.uuid4()), f'{ISSF10ARF_uuid}'),
    (3, '6-10', 'MATCH', 250, 5, False, False, 'NULL', str(uuid.uuid4()), f'{ISSF10ARF_uuid}'),
    (4, '11-12', 'MATCH', 50, 2, True, True, 1, str(uuid.uuid4()), f'{ISSF10ARF_uuid}'),
    (5, '13-14', 'MATCH', 50, 2, True, True, 1, str(uuid.uuid4()), f'{ISSF10ARF_uuid}'),
    (6, '15-16', 'MATCH', 50, 2, True, True, 1, str(uuid.uuid4()), f'{ISSF10ARF_uuid}'),
    (7, '17-18', 'MATCH', 50, 2, True, True, 1, str(uuid.uuid4()), f'{ISSF10ARF_uuid}'),
    (8, '19-20', 'MATCH', 50, 2, True, True, 1, str(uuid.uuid4()), f'{ISSF10ARF_uuid}'),
    (9, '21-22', 'MATCH', 50, 2, True, True, 1, str(uuid.uuid4()), f'{ISSF10ARF_uuid}'),
    (10, '23-24', 'MATCH', 50, 2, True, True, 1, str(uuid.uuid4()), f'{ISSF10ARF_uuid}'),
    (1, 'Sighters', 'SIGHT', 300, 'NULL', 'NULL', 'NULL', 'NULL', str(uuid.uuid4()), f'{ISSF10APF_uuid}'),
    (2, '1-5', 'MATCH', 250, 5, False, False, 'NULL', str(uuid.uuid4()), f'{ISSF10APF_uuid}'),
    (3, '6-10', 'MATCH', 250, 5, False, False, 'NULL', str(uuid.uuid4()), f'{ISSF10APF_uuid}'),
    (4, '11-12', 'MATCH', 50, 2, True, True, 1, str(uuid.uuid4()), f'{ISSF10APF_uuid}'),
    (5, '13-14', 'MATCH', 50, 2, True, True, 1, str(uuid.uuid4()), f'{ISSF10APF_uuid}'),
    (6, '15-16', 'MATCH', 50, 2, True, True, 1, str(uuid.uuid4()), f'{ISSF10APF_uuid}'),
    (7, '17-18', 'MATCH', 50, 2, True, True, 1, str(uuid.uuid4()), f'{ISSF10APF_uuid}'),
    (8, '19-20', 'MATCH', 50, 2, True, True, 1, str(uuid.uuid4()), f'{ISSF10APF_uuid}'),
    (9, '21-22', 'MATCH', 50, 2, True, True, 1, str(uuid.uuid4()), f'{ISSF10APF_uuid}'),
    (10, '23-24', 'MATCH', 50, 2, True, True, 1, str(uuid.uuid4()), f'{ISSF10APF_uuid}'),
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
    op.create_table('range_event_shooter',
    sa.Column('created_date', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('modified_date', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('firing_point', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('start_number', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('club', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('group', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('id', sqlmodel.sql.sqltypes.GUID(), nullable=False),
    sa.Column('shooting_range_id', sqlmodel.sql.sqltypes.GUID(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    schema='rcb'
    )
    op.create_index(op.f('ix_rcb_range_event_shooter_id'), 'range_event_shooter', ['id'], unique=False, schema='rcb')
    op.create_table('range_event_shot',
    sa.Column('created_date', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('modified_date', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('firing_point', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('start_number', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('series_type', sa.Enum('SIGHT', 'MATCH', 'SHOOTOFF', name='seriestype'), nullable=False),
    sa.Column('shot_id', sa.Integer(), nullable=False),
    sa.Column('shot_value', sa.Numeric(), nullable=False),
    sa.Column('shot_value_decimal', sa.Numeric(), nullable=False),
    sa.Column('x_coord', sa.Numeric(), nullable=False),
    sa.Column('y_coord', sa.Numeric(), nullable=False),
    sa.Column('id', sqlmodel.sql.sqltypes.GUID(), nullable=False),
    sa.Column('shooting_range_id', sqlmodel.sql.sqltypes.GUID(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    schema='rcb'
    )
    op.create_index(op.f('ix_rcb_range_event_shot_id'), 'range_event_shot', ['id'], unique=False, schema='rcb')
    op.create_table('range_manufactor',
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('id', sqlmodel.sql.sqltypes.GUID(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    schema='rcb'
    )
    op.create_index(op.f('ix_rcb_range_manufactor_id'), 'range_manufactor', ['id'], unique=False, schema='rcb')
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
    sa.Column('startdate', sa.DateTime(), nullable=False),
    sa.Column('enddate', sa.DateTime(), nullable=True),
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
    op.create_table('competition',
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('shortname', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('startdate', sa.DateTime(), nullable=False),
    sa.Column('enddate', sa.DateTime(), nullable=True),
    sa.Column('status', sa.Enum('CANCELLED', 'DELAYED', 'FINISHED', 'PLANNED', 'STARTED', name='competitionstatus'), nullable=False),
    sa.Column('id', sqlmodel.sql.sqltypes.GUID(), nullable=False),
    sa.Column('event_id', sqlmodel.sql.sqltypes.GUID(), nullable=False),
    sa.Column('discipline_id', sqlmodel.sql.sqltypes.GUID(), nullable=False),
    sa.Column('shooting_range_id', sqlmodel.sql.sqltypes.GUID(), nullable=True),
    sa.ForeignKeyConstraint(['discipline_id'], ['rcb.discipline.id'], ),
    sa.ForeignKeyConstraint(['event_id'], ['rcb.event.id'], ),
    sa.ForeignKeyConstraint(['shooting_range_id'], ['rcb.shooting_range.id'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='rcb'
    )
    op.create_index(op.f('ix_rcb_competition_id'), 'competition', ['id'], unique=False, schema='rcb')
    op.create_table('link_competition_range_event_shooter',
    sa.Column('range_event_shooter_id', sqlmodel.sql.sqltypes.GUID(), nullable=False),
    sa.Column('competition_id', sqlmodel.sql.sqltypes.GUID(), nullable=False),
    sa.ForeignKeyConstraint(['competition_id'], ['rcb.competition.id'], ),
    sa.ForeignKeyConstraint(['range_event_shooter_id'], ['rcb.range_event_shooter.id'], ),
    sa.PrimaryKeyConstraint('range_event_shooter_id', 'competition_id'),
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
    op.drop_table('link_competition_range_event_shooter', schema='rcb')
    op.drop_index(op.f('ix_rcb_competition_id'), table_name='competition', schema='rcb')
    op.drop_table('competition', schema='rcb')
    op.drop_index(op.f('ix_rcb_shooting_range_id'), table_name='shooting_range', schema='rcb')
    op.drop_table('shooting_range', schema='rcb')
    op.drop_index(op.f('ix_rcb_event_id'), table_name='event', schema='rcb')
    op.drop_table('event', schema='rcb')
    op.drop_index(op.f('ix_rcb_shooting_club_id'), table_name='shooting_club', schema='rcb')
    op.drop_table('shooting_club', schema='rcb')
    op.drop_index(op.f('ix_rcb_discipline_series_id'), table_name='discipline_series', schema='rcb')
    op.drop_table('discipline_series', schema='rcb')
    op.drop_index(op.f('ix_rcb_range_manufactor_id'), table_name='range_manufactor', schema='rcb')
    op.drop_table('range_manufactor', schema='rcb')
    op.drop_index(op.f('ix_rcb_range_event_shot_id'), table_name='range_event_shot', schema='rcb')
    op.drop_table('range_event_shot', schema='rcb')
    op.drop_index(op.f('ix_rcb_range_event_shooter_id'), table_name='range_event_shooter', schema='rcb')
    op.drop_table('range_event_shooter', schema='rcb')
    op.drop_index(op.f('ix_rcb_discipline_id'), table_name='discipline', schema='rcb')
    op.drop_table('discipline', schema='rcb')
    op.drop_index(op.f('ix_rcb_country_id'), table_name='country', schema='rcb')
    op.drop_table('country', schema='rcb')
    # ### end Alembic commands ###