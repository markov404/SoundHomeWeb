
from utils.abstractions.abstract_classes.abs_validators import TextValidator


class ReviewTextValidator(TextValidator):
    def __init__(self, max_lenght) -> None:
        super().__init__(max_lenght=max_lenght)

    def is_valid(self, text: str) -> bool:
        if not super().is_valid(text):
            return False
        
        if not (len(text) < self.max_lenght):
            return False 

        return True

class ReviewTitleValidator(ReviewTextValidator):
    def __init__(self) -> None:
        super().__init__(max_lenght=500)

    def is_valid(self, text: str) -> bool:
        return super().is_valid(text)


class ReviewAlbumAuthorValidator(ReviewTextValidator):
    def __init__(self) -> None:
        super().__init__(max_lenght=100)

    def is_valid(self, text: str) -> bool:
        return super().is_valid(text)


class ReviewContentValidator(ReviewTextValidator):
    def __init__(self) -> None:
        super().__init__(max_lenght=50_000)

    def is_valid(self, text: str) -> bool:
        return super().is_valid(text)
