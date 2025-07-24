import csv

from result import sort

if __name__ == "__main__":
    file_path = "packages.csv"

    # Using a list to store the data as an iterable
    data = []

    with open(file_path, mode="r") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)

    total_packages = len(data) - 1
    results = {
        'STANDARD': {
            'total': 0,
            'average_volume': 0,
            'minimum_volume': float('inf'),
            'maximum_volume': 0,
            'average_mass': 0,
            'minimum_mass': float('inf'),
            'maximum_mass': 0,
        },
        'SPECIAL': {
            'total': 0,
            'average_volume': 0,
            'minimum_volume': float('inf'),
            'maximum_volume': 0,
            'average_mass': 0,
            'minimum_mass': float('inf'),
            'maximum_mass': 0,
        },
        'REJECTED': {
            'total': 0,
            'average_volume': 0,
            'minimum_volume': float('inf'),
            'maximum_volume': 0,
            'average_mass': 0,
            'minimum_mass': float('inf'),
            'maximum_mass': 0,
        },
    }

    for item in data:
        try:
            width, height, length, mass = item
            width = int(width)
            height = int(height)
            length = int(length)
            mass = int(mass)
        except ValueError:
            continue
        category = sort(width, height, length, mass)

        if category != 'INVALID':
            results[category]['total'] += 1
            volume = width * height * length

            # check volume
            results[category]['minimum_volume'] = min(
                volume, results[category]['minimum_volume']
            )
            results[category]['maximum_volume'] = max(
                volume, results[category]['maximum_volume']
            )
            results[category]['average_volume'] += volume

            # check mass
            results[category]['minimum_mass'] = min(
                mass, results[category]['minimum_mass']
            )
            results[category]['maximum_mass'] = max(
                mass, results[category]['maximum_mass']
            )
            results[category]['average_mass'] += mass

    for category in results:
        results[category]['average_volume'] = results[category]['average_volume'] / results[category]['total']
        results[category]['average_mass'] = results[category]['average_mass'] / results[category]['total']

    print(f"Total Packages: {total_packages}")
    print()
    for category in results:
        print(f"{category}:")
        print(f"Percentage of packages: {results[category]['total'] / total_packages * 100:.2f}")
        print(f"Total: {results[category]['total']}")
        print(f"Average Volume: {results[category]['average_volume']}")
        print(f"Minimum Volume: {results[category]['minimum_volume']}")
        print(f"Maximum Volume: {results[category]['maximum_volume']}")
        print(f"Average Mass: {results[category]['average_mass']}")
        print(f"Minimum Mass: {results[category]['minimum_mass']}")
        print(f"Maximum Mass: {results[category]['maximum_mass']}")

