import imp

abstract = imp.load_source('abstract_encoder', 'code/experts/encoders/abstract_encoder.py')

class Encoder(abstract.Encoder):

    def __init__(self):
        pass