from flask.cli import FlaskGroup

from project import create_app, db
from project.api.models import Table


app = create_app()
cli = FlaskGroup(create_app=create_app)


@cli.command('recreate_db')
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command('seed_db')
def seed_db():
    """Seeds the database."""
    db.session.add(Table(
        manufacturer='Garlando',
        model='World Champion',
        photo='https://www.kickerkult.de/WebRoot/Store/Shops/61190833/4989/B842/D317/34E0/5A80/C0A8/28B8/34F0/world_champion_ml.JPG',
        price=1550
    ))
    db.session.add(Table(
        manufacturer='Leonhart',
        model='Tournament ITSF',
        photo='https://www.kickerkult.de/WebRoot/Store/Shops/61190833/6165/5CF1/3C33/3B6D/6660/55D6/982F/6634/pro-grun-schwarz_ml.jpg',
        price=1570
    ))
    db.session.add(Table(
        manufacturer='Tornado',
        model='Platinum Tour Edition ITSF',
        photo='https://www.kickerkult.de/WebRoot/Store/Shops/61190833/4987/12F2/60C2/EFB2/CE09/C0A8/28B8/3D5D/Platinum_ml.jpg',
        price=2285
    ))
    db.session.commit()


if __name__ == '__main__':
    cli()
