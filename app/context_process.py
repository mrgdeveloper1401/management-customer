class FlaskStyleUser:
    def __init__(self, user) -> None:
        self._user = user
    
    @property
    def is_authenticated(self):
        return self._user.is_authenticated if self._user else False
    
    @property
    def is_anonymous(self):
        return self._user.is_anonymous if self._user else True
    
    @property
    def is_active(self):
        return self._user.is_active if self._user else False
    
    def __getattr__(self, name):
        if self._user:
            return getattr(self._user, name)
        return None
    
    def __bool__(self):
        return self.is_authenticated
