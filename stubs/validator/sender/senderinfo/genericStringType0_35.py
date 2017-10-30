        if ( isinstance( value, BaseStrType_ ) ):
            if ( 0 <= value.__len__() <= 35 ):
                pass
            else:
                raise_value_error( value, 'Expected value between 0..35 characters' )
        else:
            for v in value:
                if ( isinstance( v, BaseStrType_ ) and 0 <= v.__len__() <= 35 ):
                    pass
                else:
                    raise_value_error( v, 'Expected value between 0..35 characters' )
        return value
