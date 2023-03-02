
from reviews.models import Review
from reviews.services.interfaces.ICommand import ICommand

class AllReviewsPageSerive(ICommand):
    
    def execute(self):
        data = self._extract_all_reviews_data_list()
        return data

    def _extract_all_reviews_data_list(self) -> list[dict]:
        output = []
        try:
            records = Review.objects.all().filter(active=True)
            for record in records:
                output.append(record.__dict__)

            if len(output) == 0:
                output = None
        except:
            output = None
        
        return output
