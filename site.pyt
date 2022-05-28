for aa in range(9):
    s = str(aa)
    with open(f'grid-{s}.html', 'wb') as f:
        print(f'file grid-{s}.html created')