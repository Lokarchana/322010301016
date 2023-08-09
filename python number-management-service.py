import requests
import json
import time

def get_numbers(urls):
  """Retrieves numbers from the specified URLs."""
  numbers = []
  for url in urls:
    start = time.time()
    response = requests.get(url, timeout=500)
    end = time.time()
    if response.status_code == 200:
      numbers.extend(json.loads(response.content)["numbers"])
    else:
      print(f"[WARNING] Skipping {url}: {response.status_code}")
  return sorted(set(numbers))

def main():
  """Starts the number-management-service."""
  port = 8008
  urls = [
      "http://20.244.56.144/numbers/primes",
      "http://abc.com/fibo",
      "http://20.244.56.144/numbers/odd"
  ]
  numbers = get_numbers(urls)
  print(json.dumps(numbers))

if _name_ == "_main_":
  main()