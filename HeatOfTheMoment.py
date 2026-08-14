import marimo

__generated_with = "0.18.3"
app = marimo.App(width="medium")


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # In the Heat of the Moment: The Acute Physiology of Cycling in a Heatwave
    In Part 1, we broke down the physics of cycling in the heat using the Power Balance Equation. We saw that when the body cannot dissipate internal heat fast enough, it accumulates, driving up core body temperature. Biology operates within the constraints set by physics.<br>
    When you ride into a heatwave without prior heat exposure, your body triggers a cascade of acute physiological emergencies. To keep your core temperature from reaching lethal levels ($>40.5^\circ\text{C}$), your autonomic nervous system executes a sharp reallocation of internal resources. Understanding this acute response reveals why your heart rate drifts higher, your legs feel empty and your functional threshold power (FTP) evaporates on a hot day. It also highlights the importance of adequate hydration and replacement of electrolytes.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
 
    """)
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <img src="https://science4performance.com/wp-content/uploads/2026/08/AridCyclist_20260812_114639.png"
     height="360" width="360">
    """)
    return


if __name__ == "__main__":
    app.run()
