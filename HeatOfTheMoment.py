# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "numpy==2.4.6",
#     "plotly==6.9.0",
# ]
# ///

import marimo

__generated_with = "0.18.3"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # In the Heat of the Moment: The Acute Physiology of Cycling in a Heatwave
    In Part 1, we broke down the physics of cycling in the heat using the Power Balance Equation. We saw that when the body cannot dissipate internal heat fast enough, it accumulates, driving up core body temperature. Now we'll explore the acute physiological responses to heat stress.<br>
    When you ride in temperatures that are significantly higher than you are used to, your body triggers a cascade of acute physiological emergencies. To keep your core temperature from reaching dangerous levels ($>40.5^\circ\text{C}$), your autonomic nervous system executes a sharp reallocation of internal resources. <br>Understanding this acute response reveals why your heart rate drifts higher, your legs feel empty and your functional threshold power (FTP) melts away on a hot day. This highlights the importance of adequate hydration and replacement of electrolytes.<br>
    Below the description of the key physiological effects, you can experiment with a simulator I built to how the body attempts to cope with a range of conditions over a four hour ride.
    """)
    return


@app.cell
def _():
    import marimo as mo
    import plotly.graph_objects as go
    from plotly.subplots import make_subplots
    import math
    return go, make_subplots, math, mo


@app.cell
def _(mo):
    mo.md("""
    <style>
    /* Responsive layout tweaks for small screens */.mo-hstack {
            flex-direction: column !important;
            gap: 16px !important;
        }
        .mo-vstack {
            width: 100% !important;
        }
        .mobile-container {
            width: 100% !important;
            padding: 0 12px !important;
            box-sizing: border-box !important;
        }
        .mobile-container .mo-vstack,
        .mobile-container .mo-hstack {
            width: 100% !important;
        }
        .mobile-container input[type="range"],
        .mobile-container input[type="number"],
        .mobile-container select,
        .mobile-container .mo-slider,
        .mobile-container .mo-switch {
            width: 100% !important;
            max-width: 100% !important;
            box-sizing: border-box !important;
        }
        .mobile-container label, .mobile-container .mo-label {
            white-space: normal !important;
        }
    }
    img, .plotly-graph-div {
        max-width: 100% !important;
        height: auto !important;
    }
    </style>
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## A Battle for Resources: Redirection of Blood Circulation
    When you are at rest in thermo-neutral conditions, your heart pumps blood around the body at about 5 L/min. Only 5-10% of this flows to the skin. Under intense exercise, cardiac output can scale up significantly to 20-30 L/min, as both the heart rate and the stoke volume blood increase. About 80-85% of blood flow is directed to skeletal muscle.<br>
    As we saw in Part 1, muscle activity generates internal heat which becomes more difficult to dissipate through the skin when the ambient temperature and humidity are high. Changes in core body temperature are detected in part of the brain called the <a href="https://en.wikipedia.org/wiki/Hypothalamus">hypothalamus</a>. Increased body heat triggers a widening of the capillary network of blood vessels (vasodilation) near the skin surface where cooling takes place. Blood flow to the skin can rise from 0.5 L/min to 7 or 8 L/min.<br>
    Since you only have a fixed amount of blood, this creates a competitive demand for blood that also needs to flow to the muscles to keep them working.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Cardiovascular Drift
    As the skin's vast network of flexible blood vessels absorbs additional blood flow, the amount of blood returning to the right atrium of the heart (venous return) decreases. This causes the amount of blood pumped out the heart (stroke volume) to fall. In order to maintain cardiac output, the heart must beat faster. Steadily rising heart rate is know as cardiovascular drift.<br>
    <a href="https://physoc.onlinelibrary.wiley.com/doi/epdf/10.1113/expphysiol.2010.054213">Studies</a> have confirmed that during acute heat exposure, heart rate tends to drift upwards by 8 to 10 bpm for every $1^\circ\text{C}$ increase in core body temperature, even when power output remains completely flat.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Losing Power
    The partial redirection of blood flow to the skin means the muscles receive less oxygenated blood. Since aerobic power is dependent on the delivery of oxygen to the muscle, the rate of oxygen use, $V&#775;O_2$, falls as core body temperature rises. This affects your $V&#775;O_2\text{max}$ and your Functional Theshold Power (FTP). Experiments show a $1.5\text{--}3.0\%$ loss per $1.0^\circ\text{C}$ rise in core body temperature above baseline.<br>
    Suppose you have an FTP of 300 W, but you are riding in heatwave conditions. If your core body temperature rises by $2^\circ\text{C}$, the same perceived effort only delivers 280 W.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Perspiration and Hydration
    In Part 1, we noted the important cooling effect of the evaporation of sweat. Eccrine sweat glands, distributed across nearly all skin surfaces, produce sweat by filtering fluid from the interstitial space, which is continuously supplied by blood plasma flowing through surrounding dermal capillaries.<br>
    The evaporation of a litre of sweat over an hour removes 2,426 kJ at a rate of 674 W. This is what an average rider would lose when pushing 200 W at 30 km/h on a $30^\circ\text{C}$ sunny day. Professional cyclists can lose 1.5 to 2.5 L/h. <br>
    As the blood plasma becomes more concentrated, it draws water by osmosis from within and around the cells of the body, helping to conserve blood volume. Nevertheless circulatory blood decreases by 100-200 mL for each litre of sweat, making it more viscous. This creates a further reduction in venous return, thereby reducing stroke volume, requiring an additional compensatory increase in heart rate (cardiac drift).<br>
    On order to conserve body fluid, the sweat response becomes less sensitive to temperature and the <a href="https://www.researchgate.net/publication/14606549_Montain_SJ_Latzka_WA_Sawka_MN_Control_of_thermoregulatory_sweating_is_altered_by_hydration_level_and_exercise_intensity_J_Appl_Physiol1995_79_1434-1439">threshold skin temperature rises</a> by $0.06^\circ\text{C}$ for every 1% of body mass fluid loss. The simulator below demonstrates how dehydration can initiate an increase in core body temperature.<br>
    This is why it is so important to maintain hydration when riding in hot conditions. Unfortunately, this is not so easy because your body can sweat much faster than your gut can absorb fluid. In normal conditions maximum gut absorption is 0.8 to 1.2 L/h, but this can fall to 0.5 to 0.7 L/h (one bottle per hour) under intense exercise in hot conditions. If you drink more, it just sloshes around in your stomach. This unavoidable fluid deficit leads to dehydration, which in turn inhibits the production of sweat for evaporative cooling. The net result is that core body temperature can rise.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Sodium Loss and Hyponatremia
    The concentration (osmotic balance) of sodium ions $Na^+$ in the blood is maintained in a relatively narrow band of 135 to 145 mmol/L. Sweat contains a range of electrolytes, primarily $Na^+$ and $Cl^-$, at relatively dilute concentrations. In an unacclimatised athlete, sodium levels are 40 to 60 mmol/L (we shall see in Part 3 that acclimatised athlete lose less sodium). Sweating causes a reduction of sodium and water from the blood plasma. <br>
    This creates a risk if you rehydrate with pure water (without electrolytes). Hyponatremia (low sodium) occurs when blood concentration falls below 135 mmol/L. This causes nausea, confusion, swelling of cells and a significant fall in endurance performance.<br>
    The key message is to rehydrate during your ride using electrolytes. For rides over 2 hours in hot weather, take one 750ml bottle of energy drink and a second 750ml bottle of water with electrolytes. For longer riders, take extra supplies to add to your bottles when you refill with water along the way.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Central Governor
    Why can't you just push through the dehydration and discomfort and carry on pumping out the power in high temperature conditions?<br>
    In a <a href="https://www.paulogentil.com/pdf/Challenging%20beliefs%20-%20ex%20Africa%20semper%20aliquid%20novi.pdf">ground-breaking paper</a> in 1997, sports scientist Professor Tim Noakes proposed what is known as The Central Governor Model. In order to prevent organ and tissue damage, the brain stimulates a sense of fatigue, designed to down-regulate the recruitment of motor units. This produces a spike in the Rate of Perceived Exertion (marathon runners can "hit the wall"). Overheating is detected in the hypothalamus. This triggers changes in neuro-chemical pathways that limit the transmission of signals to the muscles. You have to stop.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## **Simulator**
    This simulator assumes the rider has warmed up ahead of a 4 hour race/ride in hot conditions, so blood is already circulating to the skin. It shows how performance is affected when the body cannot lose enough heat to prevent a rise in core body temperature.
    """)
    return


@app.cell
def _(mo):

    def ui_sliders(mo):

        weight = mo.ui.slider(start=45, stop=100, step=1, value=70, label="Weight (kg)")
        height = mo.ui.slider(start=1.50, stop=2.00, step=0.01, value=1.78, label="Height (m)")
        power = mo.ui.slider(start=0, stop=500, step=10, value=300, label="Mechanical Power (W)")
        speed = mo.ui.slider(start=0, stop=60, step=1, value=35, label="Air Speed (km/h)")
        temp = mo.ui.slider(start=25, stop=45, step=1, value=38, label="Ambient Temp (°C)")
        humidity = mo.ui.slider(start=10, stop=100, step=5, value=55, label="Rel. Humidity (%)")
        hydration = mo.ui.slider(start=0.0, stop=1.2, step=0.1, value=1.0, label="Hydration Rate (L/hr)")
        sunny = mo.ui.switch(label="Direct sunlight", value=True)
        return height, weight, power, speed, temp, humidity, sunny, hydration


    height, weight, power, speed, temp, humidity, sunny, hydration = ui_sliders(mo)
    return height, humidity, hydration, power, speed, sunny, temp, weight


@app.cell
def _(math):
    def physics_engine(height, humidity, power, speed, temp, weight, sunny, hydration, power_penalty=0, sweat_threshold_penalty=0):
        # 1. Base Thermodynamic Constants from Part 1
        eta = 0.22 # Gross mechanical efficiency[cite: 1]
        T_s = 34.0 # Skin temperature approx (°C)[cite: 1]

        m = weight.value #[cite: 1]
        h = height.value #[cite: 1]
        P_mech = power.value * (1-power_penalty) #[cite: 1]
        v_ms = speed.value / 3.6 # km/h to m/s[cite: 1]
        T_a = temp.value #[cite: 1]
        RH = humidity.value #[cite: 1]
        intake_L_hr = hydration.value

        # 2. Body Surface Area (Du Bois formula)
        BSA = 0.20247 * (m ** 0.425) * (h ** 0.725) #[cite: 1]

        # 3. Internal Heat Generation (Watts)
        P_heat = P_mech * ((1 - eta) / eta) #[cite: 1]

        # 4. Convective Cooling
        h_c = 5.8 * (v_ms ** 0.8) #[cite: 1]
        P_conv = h_c * BSA * (T_s - T_a) #[cite: 1]

        # 5. Radiative Cooling
        h_r = 6.0 #[cite: 1]
        T_sun = 30 * sunny.value #[cite: 1]
        P_rad = h_r * BSA * 0.72 * (T_s - (T_a + T_sun)) #[cite: 1]

        # 6. Evaporative Cooling
        def P_sat(T):
            return 0.61078 * math.exp((17.27 * T) / (T + 237.3))

        P_sk_s = P_sat(T_s) #[cite: 1]
        P_a = (RH / 100) * P_sat(T_a) #[cite: 1]
        h_e = 16.5 * h_c #[cite: 1]
        P_evap_max = h_e * BSA * max(0, P_sk_s + sweat_threshold_penalty - P_a) #[cite: 1]

        P_evap_req = max(0, P_heat - P_conv - P_rad) #[cite: 1]
        P_evap = min(P_evap_req, P_evap_max) #[cite: 1]

        # 7. Net Heat Storage & Base Core Temp Drift
        P_storage = P_heat - P_conv - P_rad - P_evap #[cite: 1]
        dTc_dt = (P_storage * 3600) / (m * 3490) # °C / hr[cite: 1]

        # 8. Time-Series Projections (0 to 4 hours in 2-minute increments)
        # Latent heat of vaporization for sweat ≈ 2,430,000 J/L
        sweat_rate_L_hr = (P_evap * 3600) / 2430000 
        return dTc_dt, sweat_rate_L_hr, intake_L_hr, P_evap, P_evap_max

    def simulate(height, humidity, power, speed, temp, weight, sunny, hydration):    
        time_hours = [i * (4 / 240) for i in range(241)]
        Tc_array = []
        fluid_loss_array = []
        cv_drift_array = []
        power_delivered_array = []
        Tc = 37.4
        central_governor_stop = ""
        sweat_threshold_penalty = 0
        for t in time_hours:

            # Power Penalty (2.5% power loss per 1°C increase above 37.4°C)
            power_penalty = max(0, (Tc - 37.4) * 2.5) / 100
            power_delivered = power.value * (1 - power_penalty)
            power_delivered_array.append(power_delivered)        

            dTc_dt, sweat_rate_L_hr, intake_L_hr, P_evap, P_evap_max = physics_engine(height, humidity, power, speed, temp, weight, sunny, hydration, power_penalty, sweat_threshold_penalty)
            # Core Temp Progression, max set at 40.5, dt = 4 / 240 = 1 minute
            Tc = min(Tc + (dTc_dt * 4 / 240), 40.5)
            Tc_array.append(Tc)

            # Net Fluid Loss (Evaporated sweat - Intake)
            # Assuming wasted sweat (un-evaporated) is minimal for mathematical simplicity here
            net_loss = min(0, -(sweat_rate_L_hr - intake_L_hr) * t)
            fluid_loss_array.append(net_loss)
            sweat_threshold_penalty = (net_loss / weight.value * 100) * 0.06 # Mountain, Laztka, Sawka 1995

            # Cardiovascular Drift (~9 bpm penalty per 1°C increase above 37.4°C)
            cv_drift = max(0, (Tc - 37.4) * 9)
            cv_drift_array.append(cv_drift)
            if Tc ==40.5: 
                central_governor_stop = f"Forced to stop at<br>{int(t)} hours {(t-int(t))*60:.0f} minutes"
                break

        return time_hours, Tc_array, fluid_loss_array, cv_drift_array, power_delivered_array, sweat_rate_L_hr, P_evap, P_evap_max,central_governor_stop 
    return (simulate,)


@app.cell
def _(
    go,
    height,
    humidity,
    hydration,
    make_subplots,
    power,
    simulate,
    speed,
    sunny,
    temp,
    weight,
):
    time_hours, Tc_array, fluid_loss_array, cv_drift_array, power_delivered_array, sweat_rate_L_hr, P_evap, P_evap_max, central_governor_stop  = simulate(height, humidity, power, speed, temp, weight, sunny, hydration)

    # Precompute human-friendly time labels (h:mm) for hover display
    time_labels = [f"{int(t)}:{int((t-int(t))*60):02d}" for t in time_hours]

    # 2-Row Subplot: row1 shows Core Temp (primary) + Fluid Loss (secondary); row2 shows CV Drift (primary) + Power (secondary)
    fig = make_subplots(
        rows=2,
        cols=1,
        shared_xaxes=True,
        vertical_spacing=0.08,
        row_heights=[2, 1],
        specs=[
            [{"secondary_y": True}],
            [{"secondary_y": True}],
        ],
        subplot_titles=(
            "Core Body Temperature (°C) & Net Fluid Loss (Liters)",
            "Cardiovascular Drift (bpm penalty) & Power Delivered (Watts)",
        ),
    )

    # Trace 1: Core Temperature with formatted hover
    fig.add_trace(
        go.Scatter(
            x=time_hours,
            y=Tc_array,
            text=time_labels,
            line=dict(color='#ef4444', width=5),
            name="Core Temp",
            hovertemplate="Time: %{text}<br>Core Temp: %{y:.1f} °C<extra></extra>",
        ),
        row=1,
        col=1,
    )
    fig.add_hline(y=39.5, line_dash="dash", line_color="black", annotation_text="Critical Strain Boundary (39.5°C)", row=1, col=1)
    fig.add_hline(y=40.5, line_dash="dash", line_color="red", annotation_text="Heatstroke - Central Governor stops activity (40.5°C)", row=1, col=1)
    fig.add_annotation(x=3.5, y=38, text=central_governor_stop, showarrow=False, font=dict(size=18,color="red"),row=1, col=1)


    # Trace 2: Net Fluid Loss with formatted hover (now on secondary y-axis of row 1)
    fig.add_trace(
        go.Scatter(
            x=time_hours,
            y=fluid_loss_array,
            text=time_labels,
            line=dict(color='blue', width=5),
            name="Fluid Loss",
            fill='tozeroy',
            hovertemplate="Time: %{text}<br>Fluid Loss: %{y:.1f} L<extra></extra>",
        ),
        row=1,
        col=1,
        secondary_y=True,
    )

    # Trace 3: Cardiovascular Drift (primary y on row 2) with formatted hover
    fig.add_trace(
        go.Scatter(
            x=time_hours,
            y=cv_drift_array,
            text=time_labels,
            line=dict(color='#f59e0b', width=5),
            name="CV Drift",
            hovertemplate="Time: %{text}<br>CV Drift: %{y:.0f} bpm<extra></extra>",
        ),
        row=2,
        col=1,
        secondary_y=False,
    )

    # Trace 4: Power Delivered declines as core body temperature rises (secondary y on row 2) with formatted hover
    fig.add_trace(
        go.Scatter(
            x=time_hours,
            y=power_delivered_array,
            text=time_labels,
            line=dict(color='#8b5cf6', width=5),
            name="Power Delivered",
            hovertemplate="Time: %{text}<br>Power: %{y:.0f} W<extra></extra>",
        ),
        row=2,
        col=1,
        secondary_y=True,
    )

    fig.update_layout(
        height=680, 
        title=f"<b>Simulation: {power.value}W at {speed.value}km/h in {temp.value}°C with {humidity.value}% humidity for 4 Hours </b><br><span style='font-size: 14px; color: blue;'>Sweat Rate: {sweat_rate_L_hr:.1f} L/hr | Hydration Intake: {hydration.value:.1f} L/hr</span>",
        showlegend=False,
        margin=dict(t=80, b=40, l=60, r=40),
        hovermode="closest",
        template="plotly_white"
    )

    # Row 1 axes: Core Temp (primary) and Fluid Loss (secondary)
    fig.update_yaxes(
        range=[32.5, max(42, max(Tc_array) + 0.5)],
        row=1,
        col=1,
        secondary_y=False,
        title_text="Core Body Temperature (°C)",
        title_font=dict(color="#ef4444"),
    )
    fig.update_yaxes(
        range=[min(-8.0, min(fluid_loss_array)), max(8.0, -min(fluid_loss_array))],
        row=1,
        col=1,
        secondary_y=True,
        title_text="Net Fluid Loss (Liters)",
        title_font=dict(color="blue"),
    )

    # Row 2 axes: CV Drift (primary) and Power (secondary)
    fig.update_yaxes(
        range=[0, max(40, max(cv_drift_array) + 5)],
        row=2,
        col=1,
        secondary_y=False,
        title_text="Cardiovascular Drift (bpm penalty)",
        title_font=dict(color="#f59e0b"),
    )
    fig.update_yaxes(
        range=[min(power_delivered_array)-10, max(power_delivered_array) + 10],
        row=2,
        col=1,
        secondary_y=True,
        title_text="Power Delivered (Watts)",
        title_font=dict(color="#8b5cf6"),
    )

    fig.update_xaxes(title_text="Time (hours)", range=[0,4], row=2, col=1)
    return P_evap, P_evap_max


@app.cell
def _(
    P_evap,
    P_evap_max,
    height,
    humidity,
    hydration,
    mo,
    power,
    speed,
    sunny,
    temp,
    weight,
):
    # Provide visual feedback on sweating efficiency
    sweat_status = ""
    if P_evap >= P_evap_max and P_evap_max > 0:
        sweat_status = "⚠️ **Warning:** Evaporation is maxed out. Excess sweat will drip off and waste fluid without cooling."

    controls = mo.md("<div class='mobile-container'>")
    controls = mo.hstack(
        [
            mo.vstack(
                [
                    mo.md("### 🚴 Cycling & Hydration"),
                    power, speed, weight, height, hydration
                ]
            ),
            mo.vstack(
                [
                    mo.md("### 🌤️ Environment"),
                    sunny, temp, humidity, 
                    mo.md(sweat_status),
                ]
            ),
        ],
        gap=1,
    )
    controls
    # Return controls 
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    - The default values of the sliders (before you change them) are calibrated as a demo for an elite rider completing a 4 hour race at 300 W, travelling at 35 km/h on a sunny day at $38^\circ\text{C}$ in a sticky humidity of 55%, with a hydration rate of 1 L/hr.
        - Core body temperate remains stable for about 2 hours and then rises to $39.7^\circ\text{C}$ at the end of 4 hours, at which point power has dropped to 283 W and heart rate has drifted up 20 bpm.
        - For the first two hours, the rider was able to maintain stable core body temperature through the evaporation of sweat, at a prolific rate of 2.1 L/hr. However, net fluid loss could not be offset, even with good hydration, so that after two hours sweat rate decreased. Reduced evaporative cooling allowed core body temperature to rise.
        - Once core temperature rises, the heart rate goes up and power goes down.
        - Now, if you slide the hydration rate up to 1.2 L/hr, which is about the maximum the gut can absorb, the adverse effects are delayed, allowing the rider to maintain 290 W with a lower heart rate at the end of 4 hours.
        - Pulling hydration rate down to zero, we see that the rider is forced to stop after 2 hours and 51 minutes, due to heatstroke.
        - It might have been possible to finish the race without hydration if humidity had been a bit lower, at the risk of very severe dehydration.
        - Moving the hydration slider back to 1 L/hr and increasing speed to 45 km/h (still at 300 W), with 55% humidity, the rider benefits from greater evaporative cooling effect, due to higher Airspeed.
        - Life becomes easier if there is no direct sunlight
    - The efficiency of dissipating heat through evaporation is highly dependent
        - sweat rate, which declines as you overheat
        - relative humidity of the air: sweat evaporates better in dry air and poorly in humid air
        - the speed of air passing over the body.
    - Hydration is particularly important in hot, humid conditions without cloud cover.
    - Cyclists run the risk of not hydrating enough because the instantaneous evaporation of sweat makes the skin appear dry, removing a cue to drink more.
    - Professional cyclists use cooling jackets, cold drinks and rest their arms in ice baths in order to avoid raising core body temperature while warming up before racing in hot, humid conditions.
    - In a recent UK heatwave, I rode 134 km at 33 km/h with normalised power of 190 W in direct sunlight with air temperature of around $35^\circ\text{C}$ on the way back. I got through 3.5 large bottles, but that was only 0.5 L/hr.
        - The simulation suggests that in spite of being severely dehydrated towards the end of the ride, my sweat rate should have be sufficient to avoid overheating.
    - Apparently Filippo Ganna sat in a fridge consuming iced drinks before his hour record attempt in a hot velodrome. Humidity was deliberately raised because this reduces air density (lighter $H_2O$ displaces heavier $N_2$).
        - Set the sliders to 480 W at 60 km/h with zero hydration for a rider of 1.93 m and 83 kg. Switch off sunlight and set temperature to $35^\circ\text{C}$ and humidity to 80%.
        - The simulator suggests he'd have overheated after 50 minutes. The ride could have been prolonged to an hour by reducing core temperature below normal before the start.
    - You can experiment with the sliders to match values that interest you.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    There are limitations to this simulation. In the real life, power, speed, temperature and sun/shade are continually changing. But the key messages remain valid.<br>
    In the final part of this series Adapting to a Warmer World, we will explore how 10 to 14 days of repeated heat stress triggers physiological adaptations: expanding blood plasma volume, resetting the brain's sweating threshold and rewiring your cellular heat shock response to reclaim your lost Watts.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Technical Appendix
    The model is based on the physics engine developed in Part 1, with the addition of a rate of hydration. The simulation assumes constant ambient conditions and constant speed for a four hour ride. Calculations are performed at one minute intervals. The focus is on the point where heat can no longer be dissapated fast enough and core body temperature $T_c$ starts to rise.
    ## Sweat rate
    Latent heat of vaporization for sweat ≈ 2,430,000 J/L. To derive sweat rate from rate of heat lost from evaporation $P_{evap}$<br>
    Sweat_Rate_L_hr = ($P_{evap}$ * 3600) / 2430000
    ## Power Penalty
    2.5% power loss per 1°C increase above normal body temperature, 37.4°C. Based on current core body temperature $T_c$. See <a href="https://physoc.onlinelibrary.wiley.com/doi/epdf/10.1113/expphysiol.2010.054213">Périard</a>.<br>
    power_penalty = max(0, ($T_c$ - 37.4) * 2.5) / 100
    ## Cardiovascular Drift
    Approx 9 bpm penalty per 1°C increase above 37.4°C. See <a href="https://physoc.onlinelibrary.wiley.com/doi/epdf/10.1113/expphysiol.2010.054213">Périard</a>.<br>
    cv_drift = max(0, ($T_c$ - 37.4) * 9)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Source code for this project at https://github.com/science4performance/RidingTheHeatwave2
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
 
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
 
    """)
    return


if __name__ == "__main__":
    app.run()
