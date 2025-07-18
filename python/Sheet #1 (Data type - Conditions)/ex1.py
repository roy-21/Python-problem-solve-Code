import { useState, useEffect } from "react";
import axios from "axios";
import { BarChart, Bar, XAxis, YAxis, Tooltip, Legend, PieChart, Pie, LineChart, Line, ResponsiveContainer } from "recharts";

const CrimeReport = () => {
  const [crimeData, setCrimeData] = useState([]);

  useEffect(() => {
    axios
      .get("/api/violent-crimes/", {
        headers: { Authorization: `Bearer ${localStorage.getItem("token")}` },
      })
      .then((response) => setCrimeData(response.data))
      .catch((error) => console.error("Error fetching crime data", error));
  }, []);

  // Aggregate data for visualization
  const locationData = crimeData.reduce((acc, crime) => {
    acc[crime.location] = (acc[crime.location] || 0) + 1;
    return acc;
  }, {});

  const chartData = Object.keys(locationData).map((location) => ({
    location,
    count: locationData[location],
  }));

  return (
    <div className="grid grid-cols-2 gap-6">
      {/* Bar Chart */}
      <div className="p-4 bg-white shadow rounded-lg">
        <h2 className="text-xl font-bold mb-4">Crime Frequency by Location</h2>
        <ResponsiveContainer width="100%" height={300}>
          <BarChart data={chartData}>
            <XAxis dataKey="location" />
            <YAxis />
            <Tooltip />
            <Legend />
            <Bar dataKey="count" fill="#8884d8" />
          </BarChart>
        </ResponsiveContainer>
      </div>

      {/* Pie Chart */}
      <div className="p-4 bg-white shadow rounded-lg">
        <h2 className="text-xl font-bold mb-4">Crime Distribution</h2>
        <ResponsiveContainer width="100%" height={300}>
          <PieChart>
            <Pie data={chartData} dataKey="count" nameKey="location" cx="50%" cy="50%" outerRadius={100} fill="#82ca9d" label />
            <Tooltip />
          </PieChart>
        </ResponsiveContainer>
      </div>

      {/* Line Chart */}
      <div className="col-span-2 p-4 bg-white shadow rounded-lg">
        <h2 className="text-xl font-bold mb-4">Crime Trends Over Time</h2>
        <ResponsiveContainer width="100%" height={300}>
          <LineChart data={crimeData}>
            <XAxis dataKey="date" />
            <YAxis />
            <Tooltip />
            <Legend />
            <Line type="monotone" dataKey="victim_count" stroke="#ff7300" />
          </LineChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
};

export default CrimeReport;


import CrimeReport from "./CrimeReport";

const Dashboard = () => {
  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-6">Crime Analytics Dashboard</h1>
      <CrimeReport />
    </div>
  );
};

export default Dashboard;


import { useState, useEffect } from "react";
import axios from "axios";
import { Card, CardContent } from "@/components/ui/card";

const CrimeList = ({ crimeType }) => {
  const [crimes, setCrimes] = useState([]);

  useEffect(() => {
    axios
      .get(`/api/${crimeType}/`, {
        headers: { Authorization: `Bearer ${localStorage.getItem("token")}` },
      })
      .then((response) => setCrimes(response.data))
      .catch((error) => console.error("Error fetching crimes", error));
  }, [crimeType]);

  return (
    <div className="grid grid-cols-3 gap-4">
      {crimes.map((crime) => (
        <Card key={crime.case_id} className="p-4">
          <CardContent>
            <h2 className="text-xl font-bold">{crime.case_id}</h2>
            <p>Location: {crime.location}</p>
            <p>Date: {crime.date}</p>
            <p>{crime.description}</p>
          </CardContent>
        </Card>
      ))}
    </div>
  );
};

export default CrimeList;


from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class ViolentCrimeViewSet(viewsets.ModelViewSet):
    queryset = ViolentCrime.objects.all()
    serializer_class = ViolentCrimeSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['weapon_used', 'victim_count']
    search_fields = ['location', 'description']


from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns += [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

INSTALLED_APPS += ['rest_framework_simplejwt']

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
}

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ViolentCrimeViewSet, CyberCrimeViewSet, FraudCrimeViewSet

# Registering ViewSets with Router
router = DefaultRouter()
router.register(r'violent-crimes', ViolentCrimeViewSet)
router.register(r'cyber-crimes', CyberCrimeViewSet)
router.register(r'fraud-crimes', FraudCrimeViewSet)

urlpatterns = [
    path('api/', include(router.urls)),  # Include all routes
]

from rest_framework import viewsets
from .models import ViolentCrime, CyberCrime, FraudCrime
from .serializers import ViolentCrimeSerializer, CyberCrimeSerializer, FraudCrimeSerializer
from rest_framework.permissions import IsAuthenticated

# ViewSet for Violent Crimes
class ViolentCrimeViewSet(viewsets.ModelViewSet):
    queryset = ViolentCrime.objects.all()
    serializer_class = ViolentCrimeSerializer
    permission_classes = [IsAuthenticated]  # Requires JWT authentication

# ViewSet for Cyber Crimes
class CyberCrimeViewSet(viewsets.ModelViewSet):
    queryset = CyberCrime.objects.all()
    serializer_class = CyberCrimeSerializer
    permission_classes = [IsAuthenticated]

# ViewSet for Fraud Crimes
class FraudCrimeViewSet(viewsets.ModelViewSet):
    queryset = FraudCrime.objects.all()
    serializer_class = FraudCrimeSerializer
    permission_classes = [IsAuthenticated]

from rest_framework import serializers
from .models import ViolentCrime, CyberCrime, FraudCrime

# Base Crime Serializer
class BaseCrimeSerializer(serializers.Serializer):
    case_id = serializers.CharField()
    location = serializers.CharField()
    date = serializers.DateField()
    description = serializers.CharField()

# Specific Crime Serializers
class ViolentCrimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ViolentCrime
        fields = '__all__'

class CyberCrimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CyberCrime
        fields = '__all__'

class FraudCrimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FraudCrime
        fields = '__all__'

from django.db import models

# Base Crime model
class Crime(models.Model):
    case_id = models.CharField(max_length=50, unique=True)
    location = models.CharField(max_length=255)
    date = models.DateField()
    description = models.TextField()

    class Meta:
        abstract = True  # This makes it an abstract base class

# Violent Crime Model
class ViolentCrime(Crime):
    weapon_used = models.CharField(max_length=100)
    victim_count = models.IntegerField()

# Cyber Crime Model
class CyberCrime(Crime):
    attack_type = models.CharField(max_length=100)
    data_stolen = models.FloatField(help_text="Amount of data stolen in GB")

# Fraud Crime Model
class FraudCrime(Crime):
    fraud_type = models.CharField(max_length=100)
    financial_loss = models.DecimalField(max_digits=10, decimal_places=2)


# Base class
class Crime:
    def __init__(self, case_id, location, date):
        self.case_id = case_id
        self.location = location
        self.date = date

    def get_details(self):
        return f"Case ID: {self.case_id}, Location: {self.location}, Date: {self.date}"

# Child class for Violent Crimes
class ViolentCrime(Crime):
    def __init__(self, case_id, location, date, weapon_used, victim_count):
        super().__init__(case_id, location, date)
        self.weapon_used = weapon_used
        self.victim_count = victim_count

    def get_details(self):
        return f"{super().get_details()}, Weapon: {self.weapon_used}, Victims: {self.victim_count}"

# Child class for Cyber Crimes
class CyberCrime(Crime):
    def __init__(self, case_id, location, date, attack_type, data_stolen):
        super().__init__(case_id, location, date)
        self.attack_type = attack_type
        self.data_stolen = data_stolen

    def get_details(self):
        return f"{super().get_details()}, Attack Type: {self.attack_type}, Data Stolen: {self.data_stolen}GB"

# Usage
crime1 = ViolentCrime("VC123", "New York", "2025-02-22", "Knife", 2)
crime2 = CyberCrime("CC456", "Los Angeles", "2025-02-23", "Ransomware", 50)

print(crime1.get_details())  
# Case ID: VC123, Location: New York, Date: 2025-02-22, Weapon: Knife, Victims: 2

print(crime2.get_details())  
# Case ID: CC456, Location: Los Angeles, Date: 2025-02-23, Attack Type: Ransomware, Data Stolen: 50GB


# Base class
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_info(self):
        return f"{self.name}: ${self.price}"

# Child class: Electronics
class Electronics(Product):
    def __init__(self, name, price, brand, warranty):
        super().__init__(name, price)
        self.brand = brand
        self.warranty = warranty

    def get_info(self):
        return f"{self.name} by {self.brand} - ${self.price} ({self.warranty} year warranty)"

# Child class: Clothing
class Clothing(Product):
    def __init__(self, name, price, size, material):
        super().__init__(name, price)
        self.size = size
        self.material = material

    def get_info(self):
        return f"{self.name} ({self.size}, {self.material}) - ${self.price}"

# Usage
laptop = Electronics("Laptop", 1200, "Dell", 2)
shirt = Clothing("T-Shirt", 25, "M", "Cotton")

print(laptop.get_info())  # Laptop by Dell - $1200 (2 year warranty)
print(shirt.get_info())  # T-Shirt (M, Cotton) - $25


# Base class
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_salary(self):
        return f"{self.name}'s salary is ${self.salary}"

# Child class for Full-Time Employees
class FullTimeEmployee(Employee):
    def __init__(self, name, salary, benefits):
        super().__init__(name, salary)
        self.benefits = benefits

    def get_benefits(self):
        return f"{self.name} gets {self.benefits}"

# Child class for Part-Time Employees
class PartTimeEmployee(Employee):
    def __init__(self, name, hourly_rate, hours_worked):
        super().__init__(name, hourly_rate * hours_worked)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def get_salary(self):
        return f"{self.name}'s salary based on hours worked is ${self.salary}"

# Usage
full_time = FullTimeEmployee("Alice", 60000, "Health Insurance, Paid Leave")
part_time = PartTimeEmployee("Bob", 20, 25)  # $20 per hour, 25 hours

print(full_time.get_salary())  # Alice's salary is $60000
print(full_time.get_benefits())  # Alice gets Health Insurance, Paid Leave
print(part_time.get_salary())  # Bob's salary based on hours worked is $500


# Base class
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited ${amount}. New balance: ${self.balance}"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds!"
        self.balance -= amount
        return f"Withdrew ${amount}. New balance: ${self.balance}"

# Child class: SavingsAccount (inherits from BankAccount)
class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance=0, interest_rate=0.02):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        return f"Interest applied: ${interest}. New balance: ${self.balance}"

# Usage
savings = SavingsAccount("John Doe", 1000)
print(savings.deposit(500))  # Deposited $500. New balance: $1500
print(savings.apply_interest())  # Interest applied: $30.0. New balance: $1530.0


# Base class
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited ${amount}. New balance: ${self.balance}"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds!"
        self.balance -= amount
        return f"Withdrew ${amount}. New balance: ${self.balance}"

# Child class: SavingsAccount (inherits from BankAccount)
class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance=0, interest_rate=0.02):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        return f"Interest applied: ${interest}. New balance: ${self.balance}"

# Usage
savings = SavingsAccount("John Doe", 1000)
print(savings.deposit(500))  # Deposited $500. New balance: $1500
print(savings.apply_interest())  # Interest applied: $30.0. New balance: $1530.0

# Base class
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited ${amount}. New balance: ${self.balance}"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds!"
        self.balance -= amount
        return f"Withdrew ${amount}. New balance: ${self.balance}"

# Child class: SavingsAccount (inherits from BankAccount)
class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance=0, interest_rate=0.02):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        return f"Interest applied: ${interest}. New balance: ${self.balance}"

# Usage
savings = SavingsAccount("John Doe", 1000)
print(savings.deposit(500))  # Deposited $500. New balance: $1500
print(savings.apply_interest())  # Interest applied: $30.0. New balance: $1530.0

# Base class
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited ${amount}. New balance: ${self.balance}"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds!"
        self.balance -= amount
        return f"Withdrew ${amount}. New balance: ${self.balance}"

# Child class: SavingsAccount (inherits from BankAccount)
class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance=0, interest_rate=0.02):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        return f"Interest applied: ${interest}. New balance: ${self.balance}"

# Usage
savings = SavingsAccount("John Doe", 1000)
print(savings.deposit(500))  # Deposited $500. New balance: $1500
print(savings.apply_interest())  # Interest applied: $30.0. New balance: $1530.0


# Base class
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited ${amount}. New balance: ${self.balance}"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds!"
        self.balance -= amount
        return f"Withdrew ${amount}. New balance: ${self.balance}"

# Child class: SavingsAccount (inherits from BankAccount)
class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance=0, interest_rate=0.02):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        return f"Interest applied: ${interest}. New balance: ${self.balance}"

# Usage
savings = SavingsAccount("John Doe", 1000)
print(savings.deposit(500))  # Deposited $500. New balance: $1500
print(savings.apply_interest())  # Interest applied: $30.0. New balance: $1530.0
# Base class
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited ${amount}. New balance: ${self.balance}"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds!"
        self.balance -= amount
        return f"Withdrew ${amount}. New balance: ${self.balance}"

# Child class: SavingsAccount (inherits from BankAccount)
class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance=0, interest_rate=0.02):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        return f"Interest applied: ${interest}. New balance: ${self.balance}"

# Usage
savings = SavingsAccount("John Doe", 1000)
print(savings.deposit(500))  # Deposited $500. New balance: $1500
print(savings.apply_interest())  # Interest applied: $30.0. New balance: $1530.0
# Base class
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited ${amount}. New balance: ${self.balance}"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds!"
        self.balance -= amount
        return f"Withdrew ${amount}. New balance: ${self.balance}"

# Child class: SavingsAccount (inherits from BankAccount)
class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance=0, interest_rate=0.02):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        return f"Interest applied: ${interest}. New balance: ${self.balance}"

# Usage
savings = SavingsAccount("John Doe", 1000)
print(savings.deposit(500))  # Deposited $500. New balance: $1500
print(savings.apply_interest())  # Interest applied: $30.0. New balance: $1530.0
# Base class
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited ${amount}. New balance: ${self.balance}"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds!"
        self.balance -= amount
        return f"Withdrew ${amount}. New balance: ${self.balance}"

# Child class: SavingsAccount (inherits from BankAccount)
class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance=0, interest_rate=0.02):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        return f"Interest applied: ${interest}. New balance: ${self.balance}"

# Usage
savings = SavingsAccount("John Doe", 1000)
print(savings.deposit(500))  # Deposited $500. New balance: $1500
print(savings.apply_interest())  # Interest applied: $30.0. New balance: $1530.0
# Base class
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited ${amount}. New balance: ${self.balance}"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds!"
        self.balance -= amount
        return f"Withdrew ${amount}. New balance: ${self.balance}"

# Child class: SavingsAccount (inherits from BankAccount)
class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance=0, interest_rate=0.02):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        return f"Interest applied: ${interest}. New balance: ${self.balance}"

# Usage
savings = SavingsAccount("John Doe", 1000)
print(savings.deposit(500))  # Deposited $500. New balance: $1500
print(savings.apply_interest())  # Interest applied: $30.0. New balance: $1530.0
# Base class
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited ${amount}. New balance: ${self.balance}"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds!"
        self.balance -= amount
        return f"Withdrew ${amount}. New balance: ${self.balance}"

# Child class: SavingsAccount (inherits from BankAccount)
class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance=0, interest_rate=0.02):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        return f"Interest applied: ${interest}. New balance: ${self.balance}"

# Usage
savings = SavingsAccount("John Doe", 1000)
print(savings.deposit(500))  # Deposited $500. New balance: $1500
print(savings.apply_interest())  # Interest applied: $30.0. New balance: $1530.0
# Base class
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited ${amount}. New balance: ${self.balance}"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds!"
        self.balance -= amount
        return f"Withdrew ${amount}. New balance: ${self.balance}"

# Child class: SavingsAccount (inherits from BankAccount)
class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance=0, interest_rate=0.02):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        return f"Interest applied: ${interest}. New balance: ${self.balance}"

# Usage
savings = SavingsAccount("John Doe", 1000)
print(savings.deposit(500))  # Deposited $500. New balance: $1500
print(savings.apply_interest())  # Interest applied: $30.0. New balance: $1530.0
# Base class
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited ${amount}. New balance: ${self.balance}"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds!"
        self.balance -= amount
        return f"Withdrew ${amount}. New balance: ${self.balance}"

# Child class: SavingsAccount (inherits from BankAccount)
class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance=0, interest_rate=0.02):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        return f"Interest applied: ${interest}. New balance: ${self.balance}"

# Usage
savings = SavingsAccount("John Doe", 1000)
print(savings.deposit(500))  # Deposited $500. New balance: $1500
print(savings.apply_interest())  # Interest applied: $30.0. New balance: $1530.0
# Base class
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited ${amount}. New balance: ${self.balance}"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds!"
        self.balance -= amount
        return f"Withdrew ${amount}. New balance: ${self.balance}"

# Child class: SavingsAccount (inherits from BankAccount)
class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance=0, interest_rate=0.02):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        return f"Interest applied: ${interest}. New balance: ${self.balance}"

# Usage
savings = SavingsAccount("John Doe", 1000)
print(savings.deposit(500))  # Deposited $500. New balance: $1500
print(savings.apply_interest())  # Interest applied: $30.0. New balance: $1530.0
# Base class
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited ${amount}. New balance: ${self.balance}"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds!"
        self.balance -= amount
        return f"Withdrew ${amount}. New balance: ${self.balance}"

# Child class: SavingsAccount (inherits from BankAccount)
class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance=0, interest_rate=0.02):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        return f"Interest applied: ${interest}. New balance: ${self.balance}"

# Usage
savings = SavingsAccount("John Doe", 1000)
print(savings.deposit(500))  # Deposited $500. New balance: $1500
print(savings.apply_interest())  # Interest applied: $30.0. New balance: $1530.0
# Base class
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited ${amount}. New balance: ${self.balance}"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds!"
        self.balance -= amount
        return f"Withdrew ${amount}. New balance: ${self.balance}"

# Child class: SavingsAccount (inherits from BankAccount)
class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance=0, interest_rate=0.02):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        return f"Interest applied: ${interest}. New balance: ${self.balance}"

# Usage
savings = SavingsAccount("John Doe", 1000)
print(savings.deposit(500))  # Deposited $500. New balance: $1500
print(savings.apply_interest())  # Interest applied: $30.0. New balance: $1530.0
# Base class
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited ${amount}. New balance: ${self.balance}"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds!"
        self.balance -= amount
        return f"Withdrew ${amount}. New balance: ${self.balance}"

# Child class: SavingsAccount (inherits from BankAccount)
class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance=0, interest_rate=0.02):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        return f"Interest applied: ${interest}. New balance: ${self.balance}"

# Usage
savings = SavingsAccount("John Doe", 1000)
print(savings.deposit(500))  # Deposited $500. New balance: $1500
print(savings.apply_interest())  # Interest applied: $30.0. New balance: $1530.0
# Base class
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited ${amount}. New balance: ${self.balance}"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds!"
        self.balance -= amount
        return f"Withdrew ${amount}. New balance: ${self.balance}"

# Child class: SavingsAccount (inherits from BankAccount)
class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance=0, interest_rate=0.02):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        return f"Interest applied: ${interest}. New balance: ${self.balance}"

# Usage
savings = SavingsAccount("John Doe", 1000)
print(savings.deposit(500))  # Deposited $500. New balance: $1500
print(savings.apply_interest())  # Interest applied: $30.0. New balance: $1530.0
# Base class
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited ${amount}. New balance: ${self.balance}"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds!"
        self.balance -= amount
        return f"Withdrew ${amount}. New balance: ${self.balance}"

# Child class: SavingsAccount (inherits from BankAccount)
class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance=0, interest_rate=0.02):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        return f"Interest applied: ${interest}. New balance: ${self.balance}"

# Usage
savings = SavingsAccount("John Doe", 1000)
print(savings.deposit(500))  # Deposited $500. New balance: $1500
print(savings.apply_interest())  # Interest applied: $30.0. New balance: $1530.0
# Base class
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited ${amount}. New balance: ${self.balance}"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds!"
        self.balance -= amount
        return f"Withdrew ${amount}. New balance: ${self.balance}"

# Child class: SavingsAccount (inherits from BankAccount)
class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance=0, interest_rate=0.02):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        return f"Interest applied: ${interest}. New balance: ${self.balance}"

# Usage
savings = SavingsAccount("John Doe", 1000)
print(savings.deposit(500))  # Deposited $500. New balance: $1500
print(savings.apply_interest())  # Interest applied: $30.0. New balance: $1530.0

class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Call parent class constructor
        self.breed = breed

    def info(self):
        return f"{self.name} is a {self.breed}"

# Usage
dog = Dog("Max", "Golden Retriever")
print(dog.info())  # Output: Max is a Golden Retriever


# Parent class 1
class Animal:
    def __init__(self, name):
        self.name = name

# Parent class 2
class Pet:
    def is_pet(self):
        return True

# Child class inheriting from both Animal and Pet
class Dog(Animal, Pet):
    def speak(self):
        return f"{self.name} says: Woof!"

# Usage
dog = Dog("Rocky")
print(dog.speak())  # Output: Rocky says: Woof!
print(dog.is_pet())  # Output: True
# Base class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "I make sounds"

# Intermediate class
class Mammal(Animal):
    def has_fur(self):
        return True

# Derived class
class Dog(Mammal):
    def speak(self):
        return f"{self.name} says: Bark!"

# Usage
dog = Dog("Charlie")
print(dog.speak())  # Output: Charlie says: Bark!
print(dog.has_fur())  # Output: True
# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "I make sounds"

# Child class inheriting from Animal
class Dog(Animal):
    def speak(self):
        return f"{self.name} says: Bark!"

# Usage
dog = Dog("Buddy")
print(dog.speak())  # Output: Buddy says: Bark!
