# 🖐️ La práctica de git — tu primer ciclo completo

El objetivo de hoy es **el ciclo de git entero**, tres veces, con cambios diminutos a
propósito. La terminal es el camino titular; si se pone necia, el cuaderno
[`practica-git.ipynb`](../practica-git.ipynb) tiene los mismos pasos en celdas.

## 0 · Tu repositorio y tu clon

1. **Use this template** → nombre **`taller`** → **Public** → Create.
2. VSCode: `Ctrl+Shift+P` → **`Git: Clone`** → URL de TU repo → carpeta del home **sin
   acentos ni espacios** → *Open*.

## 1 · Las tareas antes que el código

En la web, pestaña **Issues** → abre los **tres** de
[`docs/issues-por-abrir.md`](issues-por-abrir.md), **en orden** (los números importan).

## 2 · Preséntate — tu primer commit (issue #1)

1. Di quién eres UNA vez (git firma cada foto con esto):
   ```
   git config --global user.name "Tu Nombre"
   git config --global user.email "el-correo-de-tu-cuenta-de-github"
   ```
2. En el Explorador de VSCode, dentro de `equipo/`, crea `tu-nombre.md` y escribe tus
   tres líneas (mira `jose-carlos.md` de ejemplo). Guarda.
3. El ciclo, en la terminal (`Terminal → New Terminal`):
   ```
   git status                                   # tu archivo, nuevo, en rojo
   git add equipo/tu-nombre.md
   git status                                   # ahora en verde: listo para la foto
   git commit -m "Closes #1: me presento"
   ```

## 3 · Corrige la mentira — tu segundo commit (issue #2)

1. Abre `README.md`, encuentra el dato falso de neurociencias y corrígelo. Guarda.
2. Ahora con la joya de la corona:
   ```
   git status
   git diff                                     # 👀 exactamente qué cambiaste, línea por línea
   git add README.md
   git commit -m "Closes #2: el cerebro tiene 86 mil millones"
   git log --oneline                            # tu historia: tres fotos ya
   ```

## 4 · Publica — el push (y el momento 🎉)

```
git push
```
⚠ La primera vez el navegador pedirá autorizar a VSCode con tu cuenta: dile que sí.

**DEBES VER:** al recargar la pestaña *Issues* de tu repo, **#1 y #2 CERRADOS**, cada uno
enlazado al commit que lo cerró. Eso lo hizo `Closes #N:` por ti — código y tarea quedaron
atados para siempre. En *Commits* vive tu historia, con autor y fecha.

## 5 · Para valientes (o para casa): el issue #3

* Versión directa: línea en `bitacora.md` → ciclo → `Closes #3:` → push.
* Versión valiente, **en una rama**:
  ```
  git switch -c bitacora
  # edita bitacora.md, add, commit
  git switch main        # ¡tu línea desapareció! vive en la rama
  git switch bitacora    # ¡volvió!
  git push -u origin bitacora
  ```
  y en la web GitHub te ofrecerá **Compare & pull request** — ábrelo y fusiónalo: tu
  primer PR.
* Rompe algo a propósito: borra medio README → `git restore README.md` → todo vuelve.
  Esa es la red de seguridad.

**¿Algo truena?** Copia el mensaje COMPLETO de error al grupo. Los errores también se
coleccionan. 🗂️
