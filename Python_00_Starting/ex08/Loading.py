def ft_tqdm(lst: range) -> None:

    '''\n    Decorate an iterable object,
    returning an iterator which acts exactly
    like the original iterable, but prints a dynamically updating
    progressbar every time a value is requested.\n'''

    print("Loading Bar :")
    for elem in lst:

        ratio = int(elem / len(lst) * 64)

        i = elem / len(lst) * 100

        bar = "=" * int(ratio + 1)

        print(
            f"\r{i:3.0f}%|[",
            f"{bar:64}]| {elem + 1}/{len(lst)}", end='', flush=True)

        yield elem
