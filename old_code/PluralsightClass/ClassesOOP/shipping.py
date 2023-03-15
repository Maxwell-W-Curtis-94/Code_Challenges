"""
Notes
 Scope LEGB

"""
import iso6346


class ShippingContainer:
    HEIGHT_FT = 8.5  # class attributes
    WIDTH_FT = 8.0  # class attributes

    next_serial = 1337

    def __init__(self, owner_code, length_ft, content, **kwargs):
        self.owner_code = owner_code
        self.content = content
        self.length_ft = length_ft
        self.bic = self._make_bic_code(
            owner_code=owner_code,
            serial=self._generate_serial()
        )

    @classmethod  # used when interacting with the class not an instance
    def create_empty(cls, owner_code, length_ft, **kwargs):  # **kwargs help with overriding in derived classes
        return cls(owner_code=owner_code, length_ft=length_ft, content=[], **kwargs)

    @classmethod
    def create_with_items(cls, owner_code, length_ft, content, **kwargs):
        return cls(owner_code=owner_code, length_ft=length_ft, content=list(content), **kwargs)

    @classmethod
    def _generate_serial(cls):
        """
        Requires access to the class object to call other class methods or the constructor
        """
        result = cls.next_serial
        cls.next_serial += 1
        return result

    @staticmethod  # static could be a function outside the class but makes sense to be in it
    def _make_bic_code(owner_code, serial):
        return iso6346.create(
            owner_code=owner_code,
            serial=str(serial).zfill(6)
        )

    @property  # pythons getter and setters
    def volume_ft3(self):
        return self._calc_volume()

    def _calc_volume(self):  # don't override the property override the helper function
        return ShippingContainer.HEIGHT_FT * ShippingContainer.WIDTH_FT * self.length_ft


class RefrigeratedShippingContainer(ShippingContainer):
    MAX_CELSIUS = 4.0
    FRIDGE_VOLUME_FT3 = 100

    def __init__(self, owner_code, length_ft, content, *, celsius, **kwargs):
        super().__init__(owner_code, length_ft, content, **kwargs)
        self.celsius = celsius

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(
            owner_code=owner_code,
            serial=str(serial).zfill(6),
            category="R"
        )

    @staticmethod
    def _c_to_f(celsius):
        return celsius * 9 / 5 + 32

    @staticmethod
    def _f_to_c(fahrenheit):
        return (fahrenheit - 32) * 5 / 9

    @property
    def volume_ft3(self):
        return super()._calc_volume() - RefrigeratedShippingContainer.FRIDGE_VOLUME_FT3

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        self._set_celsius(value)

    def _set_celsius(self, value):
        if value > RefrigeratedShippingContainer.MAX_CELSIUS:
            raise ValueError("Temperature too hot!")
        self._celsius = value

    @property
    def fahrenheit(self):
        return RefrigeratedShippingContainer._c_to_f(self.celsius)

    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = RefrigeratedShippingContainer._f_to_c(value)


class HeatedRefrigeratedShippingContainer(RefrigeratedShippingContainer):
    MIN_CELSIUS = -20

    def _set_celsius(self, value):
        if value < HeatedRefrigeratedShippingContainer.MIN_CELSIUS:
            raise ValueError("Temperature to cold")
        super()._set_celsius(value)
