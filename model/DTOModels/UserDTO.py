from entity.UserEntity import UserEntity

class UserDTO:

    def __init__(self):
        self.id = None
        self.firstName = None
        self.lastName = None
        self.username = None
        self.password = None
        self.position = None

    @staticmethod
    def createFromEntity(entity: UserEntity):
        userDTO = UserDTO()
        userDTO.id = entity.id
        userDTO.firstName = entity.firstName
        userDTO.lastName = entity.lastName
        userDTO.username = entity.username
        userDTO.password = entity.password
        userDTO.position = entity.position

    def __repr__(self):
        return str(self.__dict__)