        if ( isinstance( value, BaseStrType_ ) and value.__len__() == 2 and value in [ 'FI', 'SV', 'EN' ]):
            pass
        else:
            raise_value_error( value, 'Expected ISO 639-1' )
        return value
