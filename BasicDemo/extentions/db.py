from flask_sqlalchemy import SQLAlchemy as _BaseSQLAlchemy


class SQLAlchemy(_BaseSQLAlchemy):
    def apply_driver_hacks(self, app, info, options):
        if info.drivername == "mysql+mysqlconnector":
            options["connect_args"] = {"time_zone": "+0:00"}
        options.update({"pool_pre_ping": True})
        super(SQLAlchemy, self).apply_driver_hacks(app, info, options)


db = SQLAlchemy()
