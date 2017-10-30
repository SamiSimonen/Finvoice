        import re
        if ( isinstance( value, BaseStrType_ ) ):
            if ( re.match( '[1-9]?[0-9]{1,2}(,[0-9]{1,3})?', value ) ):
                pass
            else:
                raise_value_error( value, 'Expected value in the format [1-9]?[0-9]{1,2}(,[0-9]{1,3})?' )
        else:
            for v in value:
                if ( isinstance( v, BaseStrType_ ) and re.match( '[1-9]?[0-9]{1,2}(,[0-9]{1,3})?', value) ):
                    pass
                else:
                    raise_value_error( v, 'Expected value in the format [1-9]?[0-9]{1,2}(,[0-9]{1,3})?' )
        return value
