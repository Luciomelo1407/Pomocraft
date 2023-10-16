
class TimeTransform:

    def transform(self,time):
        if time > 9:
            return str(time)
        return '0' + str(time)
