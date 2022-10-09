import RPi.GPIO as GPIO
import time
import random

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(20, GPIO.OUT)  # rojoLED
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Rojo

GPIO.setup(24, GPIO.OUT)  # VerdeLED
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Verde

GPIO.setup(23, GPIO.OUT)  # amarilloLED
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Amarillo

GPIO.setup(18, GPIO.OUT)  # azulLED
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Azul

instructions_list = [2, 4, 1]


def lost_animation_complete():
    lose_animation_sequence()
    lose_animation_sequence()
    lose_animation_blink()
    lose_animation_blink()


def lose_animation_sequence():
    GPIO.output(20, True)
    time.sleep(.1)
    GPIO.output(20, False)
    GPIO.output(24, True)
    time.sleep(.1)
    GPIO.output(24, False)
    GPIO.output(23, True)
    time.sleep(.1)
    GPIO.output(23, False)
    GPIO.output(18, True)
    time.sleep(.1)
    GPIO.output(18, False)


def lose_animation_blink():
    GPIO.output(20, True)
    GPIO.output(24, True)
    GPIO.output(23, True)
    GPIO.output(18, True)
    time.sleep(.3)
    GPIO.output(20, False)
    GPIO.output(24, False)
    GPIO.output(23, False)
    GPIO.output(18, False)
    time.sleep(.3)


def main():
    lost_animation_complete()
    game()
    lost_animation_complete()


def turn_led_on(led):
    print("Turning led ")
    if led == 1:
        print("num1\n")
        GPIO.output(20, True)
        time.sleep(0.8)
        GPIO.output(20, False)
    elif led == 2:
        print("num2\n")
        GPIO.output(24, True)
        time.sleep(0.8)
        GPIO.output(24, False)
    elif led == 3:
        print("num3\n")
        GPIO.output(23, True)
        time.sleep(0.8)
        GPIO.output(23, False)
    elif led == 4:
        print("num4\n")
        GPIO.output(18, True)
        time.sleep(0.8)
        GPIO.output(18, False)
    time.sleep(0.3)


def turn_leds_on():
    for led in instructions_list:
        turn_led_on(led)


def listening():
    index = 0
    player_succeeded = True
    is_any_button_pressed = False
    tic = time.perf_counter()
    print("Tiempo {}".format(tic))
    while not index == len(instructions_list):
        if not is_any_button_pressed:
            button_red_released = GPIO.input(21)
            if not button_red_released:
                tic = time.perf_counter()
                is_any_button_pressed = True
                GPIO.output(20, True)

                if not instructions_list[index] == 1:
                    player_succeeded = False
                    break
                index += 1
            else:
                GPIO.output(20, False)

            button_green_released = GPIO.input(16)
            if not button_green_released:
                tic = time.perf_counter()
                is_any_button_pressed = True
                GPIO.output(24, True)
                if not instructions_list[index] == 2:
                    player_succeeded = False
                    break
                index += 1
            else:
                GPIO.output(24, False)

            button_yellow_released = GPIO.input(12)
            if not button_yellow_released:
                tic = time.perf_counter()
                is_any_button_pressed = True
                GPIO.output(23, True)
                if not instructions_list[index] == 3:
                    player_succeeded = False
                    break
                index += 1
            else:
                GPIO.output(23, False)

            button_blue_released = GPIO.input(4)
            if not button_blue_released:
                tic = time.perf_counter()
                is_any_button_pressed = True
                GPIO.output(18, True)
                if not instructions_list[index] == 4:
                    player_succeeded = False
                    break
                index += 1
            else:
                GPIO.output(18, False)
        elif GPIO.input(21) and GPIO.input(16) and GPIO.input(12) and GPIO.input(4):
            is_any_button_pressed = False
        if time.perf_counter() - tic > 3:
            player_succeeded = False
            break
    time.sleep(0.3)
    GPIO.output(20, False)
    GPIO.output(24, False)
    GPIO.output(23, False)
    GPIO.output(18, False)
    time.sleep(0.3)

    return player_succeeded


def game():
    while True:
        instruction = random.randint(1, 4)
        instructions_list.append(instruction)
        turn_leds_on()
        if not listening():
            break


def game_test():
    while True:
        boton_estado_rojo = GPIO.input(21)
        if boton_estado_rojo == False:
            GPIO.output(20, True)
        else:
            GPIO.output(20, False)

        boton_estado_verde = GPIO.input(16)
        if boton_estado_verde == False:
            GPIO.output(24, True)
        else:
            GPIO.output(24, False)

        boton_estado_amarillo = GPIO.input(12)
        if boton_estado_amarillo == False:
            GPIO.output(23, True)
        else:
            GPIO.output(23, False)

        boton_estado_azul = GPIO.input(4)
        if boton_estado_azul == False:
            GPIO.output(18, True)
        else:
            GPIO.output(18, False)


if __name__ == "__main__":
    main()
