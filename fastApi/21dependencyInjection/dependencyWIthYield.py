from fastapi import Depends


def generate_dep_a():
    pass


def generate_dep_b():
    pass


def generate_dep_c():
    pass


async def dependency_a():
    dep_a = generate_dep_a()
    try:
        yield dep_a
    finally:
        dep_a.close()


async def dependency_b(dep_a=Depends(dependency_a)):
    dep_b = generate_dep_b()
    try:
        yield dep_b
    finally:
        dep_b.close(dep_a)


async def dependency_c(dep_b=Depends(dependency_b)):
    dep_c = generate_dep_c()
    try:
        yield dep_c
    finally:
        dep_c.close()



async def get_dp():
    db = DBSession()
    try:
        yield db
    finally:
        db.close()


"""
FastAPI will make sure that the "exit code" in each dependency with
yield is run in the correct order.
"""