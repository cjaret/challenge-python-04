def div(func):
    def wrapper(*args, **kwargs):        
        strx = func(*args, **kwargs)
        strx = f'<div> {strx} </div>'
        return strx
    return wrapper


def article(func):
    def wrapper(*args, **kwargs):        
        strx = func(*args, **kwargs)
        strx = f'<article> {strx} </article>'
        return strx
    return wrapper


def p(func):
    def wrapper(*args, **kwargs):        
        strx = func(*args, **kwargs)
        strx = f'<p> {strx} </p>'
        return strx
    return wrapper


# Here you must apply the decorators, uncomment this later

@div
@article
@p
def saludo(nombre):
    return f'¡Hola {nombre}, ¿Cómo estás?'


def run():
    print(saludo('Jorge'))


if __name__ == '__main__':
    run()

# → We want to have →three← different outputs 👇🏼

# <div>¡Hola Jorge, ¿Cómo estás?'</div>
# <article>¡Hola Jorge, ¿Cómo estás?'</article>
# <p>¡Hola Jorge, ¿Cómo estás?'</p>
