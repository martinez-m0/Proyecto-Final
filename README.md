# Proyecto-Final
# Diagrama De Flujo
```mermaid
flowchart TD
    A[Inicio] --> B[Elegir dificultad]
    B --> C{¿Dificultad válida?}
    C -- No --> B
    C -- Sí --> D[Cargar palabras desde archivo según dificultad]
    D --> E[Elegir palabra al azar]
    E --> F[Inicializar variables: fallos, resultado, letras_todas]
    F --> G{¿Juego terminado?}
    
    G -- Sí: Ganaste --> H[Mostrar mensaje de victoria]
    G -- Sí: Perdiste --> I[Mostrar mensaje de derrota y palabra]

    G -- No --> J[Mostrar interfaz del juego]
    J --> K[Imprimir muñeco o estructura base]
    K --> L[Mostrar letras adivinadas]

    L --> M[Solicitar letra al usuario]
    M --> N{¿Letra válida y no repetida?}
    N -- No --> M
    N -- Sí --> O[Agregar letra a letras_todas]

    O --> P{¿Letra está en palabra?}
    P -- Sí --> Q[Actualizar letras acertadas en resultado]
    Q --> G

    P -- No --> R[Incrementar fallos]
    R --> G

    H --> Z[Fin]
    I --> Z[Fin]
