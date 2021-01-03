from rest_framework.test import APITestCase
from price_models.models import PriceModel
from rental_objects.models import RentalObject
from reservations.api.serializers import ReservationSerializer
from reservations.models import Reservation
from users.models import NotRegisteredUser
from django.core.exceptions import ValidationError
# TODO Reservation Endpunkte erstellen, price_model soll bei Reservierungen zugewiesen werden
# TODO Prperties zu Mietobjekte erstellen können


class ReservationTests(APITestCase):
    fixtures = ["reservations/api/fixtures/manufacturers.json", "reservations/api/fixtures/cars.json",
                "reservations/api/fixtures/price_models.json", "reservations/api/fixtures/prices.json",
                "reservations/api/fixtures/rental_objects.json", ]

    def setUp(self):
        self.price_model = PriceModel.objects.get(pk=1)
        self.rental_object = RentalObject.objects.get(pk=1)

    def test_reservation_can_be_created(self):
        address_data = {"street": "Some Streeet", "house_number": "122", "postal_code": "443543", "location": "City12"}

        profile = {"address": address_data}

        not_registered_user_data = {"first_name": "Tom", "last_name": "Smith", "email": "testmail@nomail.com",
                                    "profile": profile
                                    }

        data = {"rental_object": self.rental_object.id, "price_model": self.price_model.id,
                "pick_up_datetime": "2021-01-01 17:30", "return_datetime": "2021-01-02 17:30",
                "not_registered_user": not_registered_user_data,
                "user": None,
                }

        print(data)

        response = self.client.post("/api/v1/reservations/", data=data, format="json")

        self.assertEqual(response.status_code, 201, "response.status_code should be 201")
        self.assertEqual(Reservation.objects.count(), 1, "Reservation.objects.count() should be 1")

        new_reservation_instance = Reservation.objects.get(pk=1)

        self.assertEqual(
            new_reservation_instance.not_registered_user.first_name, not_registered_user_data.get("first_name")
        )

        self.assertEqual(
            new_reservation_instance.not_registered_user.last_name, not_registered_user_data.get("last_name")
        )

        self.assertEqual(
            new_reservation_instance.not_registered_user.email, not_registered_user_data.get("email")
        )

        self.assertEqual(
            new_reservation_instance.not_registered_user.profile.address.street, address_data.get("street")
        )

        self.assertEqual(
            new_reservation_instance.not_registered_user.profile.address.house_number, address_data.get("house_number")
        )

        self.assertEqual(
            new_reservation_instance.not_registered_user.profile.address.postal_code, address_data.get("postal_code")
         )


class ReservationExceptionTests(APITestCase):
    fixtures = ["reservations/api/fixtures/manufacturers.json", "reservations/api/fixtures/cars.json",
                "reservations/api/fixtures/price_models.json", "reservations/api/fixtures/prices.json",
                "reservations/api/fixtures/rental_objects.json", "reservations/api/fixtures/not_registered_users.json",
                "reservations/api/fixtures/addresses.json", "reservations/api/fixtures/reservations.json",
                ]

    def setUp(self):
        self.reservation = Reservation.objects.get(pk=1)
        self.rental_object = RentalObject.objects.get(pk=1)

    def test_Should_FailToCreate_When_PriceIsAssignedToReservationThatIsNotPartOfRentalObjectsPriceModels(self):
        self.assertIn(self.reservation.price_model, self.rental_object.price_models.all())

        wrong_price_model = PriceModel.objects.get(pk=2)

        self.reservation.price_model = wrong_price_model

        data = ReservationSerializer(instance=self.reservation).data

        reservation_serializer = ReservationSerializer(
            instance=self.reservation, data=data
        )

        self.assertEqual(False, reservation_serializer.is_valid())


# Should_ExpectedBehavior_When_StateUnderTest
# Should_ThrowException_When_AgeLessThan18


# https://dzone.com/articles/7-popular-unit-test-naming
