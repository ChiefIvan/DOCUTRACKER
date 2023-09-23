<script>
  // @ts-nocheck

  import { fade } from "svelte/transition";
  import {
    serverResponse,
    resetInput,
    captchaVerification,
    captchaAttemps,
  } from "../../stores";

  import Input from "./input.svelte";

  let bytesIO = {};
  let id = "";
  let byteValue = "";
  let userCaptGenVal = "";

  export let checkboxDisabled = true;

  const captchaAPI = "http://127.0.0.1:5000/captcha";

  async function handleGETCaptcha() {
    $captchaAttemps--;

    if ($captchaAttemps < 0) {
      $serverResponse = {
        error: "Captcha Verification Failed!, Please Try Again.",
      };

      $captchaAttemps = 3;
      return;
    }

    await fetch(captchaAPI, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
    })
      .then((response) => response.json())
      .then((data) => (bytesIO = data.captcha))
      .catch(
        () =>
          ($serverResponse = {
            error: "Server is down, please try again later.",
          })
      );

    id = bytesIO[1];
    byteValue = bytesIO[0];

    localStorage.setItem("captchaId", id);
  }

  async function handlePOSTCaptcha() {
    $resetInput.blur();

    let userCaptCredentials = {
      captValue: userCaptGenVal,
      captchaId: localStorage.getItem("captchaId") || "",
    };

    try {
      const captAPIres = await fetch(captchaAPI, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(userCaptCredentials),
      });

      if (captAPIres.ok) {
        const data = await captAPIres.json();
        if (Object.keys(data) == "success") {
          $captchaVerification = data["success"];
          checkboxDisabled = $captchaVerification && true;
        } else {
          setTimeout(() => {
            handleGETCaptcha();
          }, 1000);
        }
      }
    } catch {
      $serverResponse = {
        error: "Server is down, please try again later.",
      };
    }

    byteValue = "";
    userCaptGenVal = "";
  }
</script>

{#if byteValue.length !== 0}
  <div class="capt-img-wrapper" transition:fade={{ delay: 100, duration: 400 }}>
    <form on:submit|preventDefault={handlePOSTCaptcha}>
      <img src={`data:image/jpeg;base64,${byteValue}`} alt="" />
      <Input
        inputName={"Captcha"}
        inputType={"text"}
        inputAutocomplete={"off"}
        inputValue={userCaptGenVal}
        inputZ={"2"}
        inputSize={"100%"}
        on:input={(e) => (userCaptGenVal = e.target.value)}
      />
      <div class="btn-wrapper">
        <button>Submit</button>
      </div>
    </form>
  </div>
{/if}

<div
  class:container-disabled={checkboxDisabled}
  title={checkboxDisabled ? "Please fill all entries first" : ""}
>
  <div class="checkbox-wrapper">
    <span>
      <input
        id="remember"
        type="checkbox"
        checked={$captchaVerification}
        class:got-checked={$captchaVerification}
        on:change={handleGETCaptcha}
        disabled={checkboxDisabled}
        bind:this={$resetInput}
      />
      <svg class:got-checked={$captchaVerification}>
        <use xlink:href="#checkbox-30" class="checkbox" />
      </svg>
    </span>
    <svg
      class:got-checked={$captchaVerification}
      xmlns="http://www.w3.org/2000/svg"
      style="display:none"
    >
      <symbol id="checkbox-30" viewBox="0 0 22 22">
        <path
          fill="none"
          stroke="blue"
          d="M5.5,11.3L9,14.8L20.2,3.3l0,0c-0.5-1-1.5-1.8-2.7-1.8h-13c-1.7,0-3,1.3-3,3v13c0,1.7,1.3,3,3,3h13 c1.7,0,3-1.3,3-3v-13c0-0.4-0.1-0.8-0.3-1.2"
        />
      </symbol>
    </svg>
  </div>
  <label for="remember">I am not a robot</label>
</div>

<style>
  div.capt-img-wrapper {
    z-index: 1;
    position: fixed;
    inset: 0;
    cursor: default;

    display: flex;
    justify-content: center;
    align-items: center;

    & form {
      display: flex;
      align-items: flex-start;
      justify-content: center;
      flex-direction: column;
      row-gap: 1rem;

      background-color: white;
      padding: 0.5rem;
      box-shadow: 5px 5px 25px gray;
      border-radius: 1rem;

      & div.btn-wrapper {
        width: 100%;
        display: flex;
        justify-content: flex-end;
      }
    }
  }

  div {
    display: flex;
    column-gap: 0.5rem;

    & label {
      cursor: pointer;
      transition: all calc(var(--dur) / 3) ease-in-out;
      color: gray;
    }

    & .checkbox-wrapper {
      & span {
        display: inline-block;
        min-width: calc(var(--size, 1) * 20px);
        position: relative;

        & svg {
          fill: none;
          left: 0;
          pointer-events: none;
          stroke: var(--stroke, var(--border-active));
          stroke-dasharray: var(--dashArray, 93);
          stroke-dashoffset: var(--dashOffset, 94);
          stroke-linecap: round;
          stroke-linejoin: round;
          stroke-width: 2px;
          top: 0;
          transition: stroke-dasharray var(--dur), stroke-dashoffset var(--dur);
        }

        & svg,
        input {
          display: block;
          height: 100%;
          width: 100%;
        }
      }

      & span:after {
        content: "";
        width: 100%;
        padding-top: 100%;
        display: block;
      }

      & input {
        -webkit-appearance: none;
        -moz-appearance: none;
        -webkit-tap-highlight-color: transparent;
        cursor: pointer;
        background-color: var(--bg);
        border-radius: calc(var(--size, 1) * 4px);
        border: calc(var(--newBrdr, var(--size, 1)) * 1px) solid;
        color: var(--brdr);
        outline: none;
        margin: 0;
        padding: 0;
        transition: all calc(var(--dur) / 3) linear;
      }

      & input.got-checked {
        color: var(--newBrdrClr);
      }

      & input:hover,
      input:checked {
        --newBrdr: var(--size, 1);
      }

      & input:checked {
        --newBrdrClr: var(--brdr-actv);
        transition-delay: calc(var(--dur) / 1.3);
      }
    }

    & .checkbox-wrapper span > * {
      position: absolute;
    }

    & .checkbox-wrapper span input:checked + svg.got-checked {
      --dashArray: 16 93;
      --dashOffset: 109;
    }
  }

  div.container-disabled {
    cursor: not-allowed;
  }

  div:hover label {
    color: var(--brdr-hovr);
  }

  div.container-disabled:hover input {
    cursor: not-allowed;
  }

  div.container-disabled:hover label {
    cursor: not-allowed;
    color: gray;
  }
</style>
