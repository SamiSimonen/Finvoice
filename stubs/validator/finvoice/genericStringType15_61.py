        if ( isinstance( value, BaseStrType_ ) ):
            if ( 15 <= value.__len__() <= 61 ):
                pass
            else:
                raise_value_error( value, 'Expected value between 15..61 characters' )
        else:
            for v in value:
                if ( isinstance( v, BaseStrType_ ) and 15 <= v.__len__() <= 61 ):
                    pass
                else:
                    raise_value_error( v, 'Expected value between 15..61 characters' )
        return value
