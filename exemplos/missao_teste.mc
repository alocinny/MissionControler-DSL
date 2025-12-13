mission "Competição SAE 2025" {

    settings {
        max_altitude: 30.0          # metros
        base_speed: 6.0             # m/s
        failsafe_battery: 20        # inteiro de 10 a 30
    }

    waypoints {
        "Home"          : -27.6037, -48.5191
        "Ponto A"       : -27.5920, -48.5520, 20.0
        "Ponto B"       : -27.5930, -48.5530, 18.0
        "Zona Carga"    : -27.5940, -48.5540, 15.0
    }

    start {
        takeoff(12.0)
        speed(5.0)
    }

    task "Ir até zona" {
        goto("Ponto A")
        goto("Ponto B")
        goto("Zona Carga")
        hover(5)
    }

    task "Soltar e voltar" {
        hover(3)
        rtl()
    }

    end {
        land()
    }
}

