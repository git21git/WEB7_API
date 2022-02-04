import argparse
from Helper.mapapi_PG import show_map
from Helper.geocoder import get_ll_span


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("coords", help="Введите 2 числа через запятую, без пробела")
    parser.add_argument("spn", help="Введите 2 числа через запятую, без пробела")
    args = parser.parse_args()
    ll, spn = get_ll_span(args.coords)
    # spn = input('Масштаб введите, уважаемый-с')

    show_map(f'll={ll}&spn={args.spn}')

# python main.py 2.2945111,48.8582573 0.016457,0.00619
# 2.2945111, 48.8582573
# 0.016457,0.00619


if __name__ == '__main__':
    main()
