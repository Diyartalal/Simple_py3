def adjacentElementsProduct(l):
    return(max(x * y for x, y in zip(l, l[1:])))
