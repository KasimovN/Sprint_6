from data import Scooter


class Helper:
    @staticmethod
    def parametrize_massive_qa():
        massive = []
        for i in range(len(Scooter.QUESTIONS)):
            massive.insert(i, (Scooter.QUESTIONS[i], Scooter.ANSWERS[i]))
        return massive

    @staticmethod
    def parametrize_massive_order():
        massive = []
        for i in range(len(Scooter.NAME)):
            massive.insert(i, (Scooter.NAME[i], Scooter.SURNAME[i], Scooter.ADDRESS[i],
                               Scooter.METRO_STATION[i], Scooter.TELEPHONE[i], Scooter.COMMENT[i]))
        return massive
