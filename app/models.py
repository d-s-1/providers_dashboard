from app import db


# (indexed the columns that feed dropdowns so that dropdown options will update faster as users are making selections; indexing these columns should also speed up
# other queries as these columns are used to filter the data set.)
class Utilization(db.Model):
    record_id = db.Column(db.Integer, primary_key=True)
    provider_id = db.Column(db.Integer, index=True)
    credential = db.Column(db.String(25), index=True)
    city = db.Column(db.String(35), index=True)
    zip_code = db.Column(db.String(5), index=True)
    state = db.Column(db.String(2), index=True)
    provider_type = db.Column(db.String(50), index=True)
    place_of_service = db.Column(db.String(15), index=True)
    hcpcs_code = db.Column(db.String(5), index=True)
    hcpcs_desc = db.Column(db.String(260))
    num_beneficiaries = db.Column(db.Integer)
    avg_allowed = db.Column(db.Float(precision=9))
    avg_charged = db.Column(db.Float(precision=9))
    avg_paid = db.Column(db.Float(precision=9))

    def __repr__(self):
        return '<Utilization {}>'.format(self.record_id)