from Helper.mapapi_PG import show_map
from Helper.geocoder import get_ll_span

coords = input('Введите координаты через запятую без пробела: ')
ll, spn = get_ll_span(coords)
show_map(f'll={ll}&spn={spn}')
