mission "Teste Erro Sintaxe" {

    settings {
        max_altitude: 30.0          # metros
        base_speed: 6.0             # m/s
        failsafe_battery: 20        # inteiro de 10 a 30
    
    
    waypoints 
        "Home"           -27.6037, -48.5191
        "Ponto Alvo"    : -27.5950, -48.5550, 15.0
    

    start {
        takeoff(10.0)
    }

    task "Ir e voltar" {
        goto("Ponto Alvo")
        rl(
    

    end {
        land()
    }