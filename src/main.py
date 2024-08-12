from bson import ObjectId

from src.domain.__shared.entity import UniqueEntityId

print({"message": f'{UniqueEntityId(id=ObjectId())}'})
