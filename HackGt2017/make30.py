import django
django.setup()

from delta.models import Profile, Seat


def main():
	Seat.objects.all().delete()

	for x in range(1,31):
		s = Seat(number=x)
		s.save()


if __name__ == "__main__":
	main()
