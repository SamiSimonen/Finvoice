        import re
        if ( isinstance( value, BaseStrType_ ) ):
            if ( re.match( '[0-9]{1,15}(,[0-9]{1,6})?', value ) ):
                pass
            else:
                raise_value_error( value, 'Expected value in the format [0-9]{1,15}(,[0-9]{1,6})?' )
        else:
            for v in value:
                if ( isinstance( v, BaseStrType_ ) and re.match( '[0-9]{1,15}(,[0-9]{1,6})?', value) ):
                    pass
                else:
                    raise_value_error( v, 'Expected value in the format [0-9]{1,15}(,[0-9]{1,6})?' )
        return value
