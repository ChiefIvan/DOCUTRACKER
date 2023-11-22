<script lang="ts">
  import {
    type LoginBind,
    type ResponseData,
    handleFetch,
    address,
    showMessage,
  } from "../../store";
  import { Link, navigate } from "svelte-routing";
  import { Timer } from "../shared/Timer";

  import logoElegant from "./../../assets/transparent-favicon-elegant.png";
  import Input from "../shared/Input.svelte";
  import Button from "../shared/Button.svelte";
  import CheckBox from "../shared/CheckBox.svelte";
  import BarLoader from "../shared/BarLoader.svelte";

  let isRequest = false;
  let bindForm: HTMLFormElement;
  let LoginAttemps = 2;

  const loginTimer = new Timer();
  loginTimer.checkTimer(300_000, "tl");

  const resendTimer = new Timer();
  resendTimer.checkTimer(120_000, "rl");

  $: disabled = $loginTimer <= 0;
  $: disabledResend = $resendTimer <= 0;

  $: if (disabled) {
    LoginAttemps = 2;
  }

  const loginAddress = `${address}/login`;
  const loginMethod = "POST";

  $: loginUser = {
    email: "",
    password: "",
    btnDisabled: !disabled,
  };

  let inputBinds: LoginBind = {
    emailInput: false,
    passwordInput: false,
  };

  $: loginRequest = {
    method: loginMethod,
    address: loginAddress,
    credentials: loginUser,
  };

  const handleSubmit = async () => {
    isRequest = true;

    try {
      const response: ResponseData = await handleFetch(loginRequest);

      bindForm.reset();
      (document.activeElement as HTMLElement).blur();

      inputBinds = {
        emailInput: false,
        passwordInput: false,
      };

      if (response.error) {
        $showMessage = response;

        if (LoginAttemps <= 0) {
          if ($loginTimer <= 0) {
            loginTimer.startTimer(300, "tl");
          }

          isRequest = false;
          return;
        }

        LoginAttemps--;
      }

      if (response.remembered) {
        sessionStorage.setItem("remember", response.remembered);
        window.location.href = "/dashboard";
      }

      isRequest = false;
    } catch (error) {
      console.error(error);
      isRequest = false;
    }
  };

  const handleInput = (event: Event) => {
    const target = event.target as HTMLInputElement;
    const id = target.id;

    if (id === "Email") {
      loginUser.email = target.value;
    }

    if (id === "Password") {
      loginUser.password = target.value;
    }
  };

  let remember = false;
  const handleChange = () => {
    remember = !remember;
  };

  const resendAddress = `${address}/resend`;
  const resendMethod = "POST";

  $: setStylesDisabled = !disabledResend;

  $: resendRequest = {
    method: resendMethod,
    address: resendAddress,
    credentials: {
      email: localStorage.getItem("email") || "",
      btnDisabled: !disabledResend,
    },
  };

  const handleResend = async () => {
    setStylesDisabled = true;

    if (resendRequest.credentials && !resendRequest.credentials.email?.length) {
      $showMessage = { error: "Please Sign Up First!" };
      navigate("/auth/signup");
      return;
    }

    try {
      const response: ResponseData = await handleFetch(resendRequest);

      if (response.error || response.success) {
        setStylesDisabled = false;
        $showMessage = response;
        return;
      }
      resendTimer.startTimer(120, "rl");
    } catch (error) {
      setStylesDisabled = false;
      console.error(error);
    }
  };
</script>

<svelte:head>
  <title>DOCUTRACKER | Login</title>
</svelte:head>

{#if isRequest}
  <BarLoader />
{/if}

<main>
  <div class="form-container">
    <form
      bind:this={bindForm}
      class="form"
      on:submit|preventDefault={handleSubmit}
    >
      <img class="favicon-elegant" src={logoElegant} alt="Docutracker's Logo" />
      <div class="title-container">
        <h1>Welcome back</h1>
        <p>
          Don't have an account?
          <Link to="/auth/signup"><span>Signup</span></Link>
        </p>
      </div>
      <Input
        inputType="email"
        inputName="Email"
        on:input={handleInput}
        bind:focusedInput={inputBinds.emailInput}
      />
      <Input
        inputType="password"
        inputName="Password"
        on:input={handleInput}
        bind:focusedInput={inputBinds.passwordInput}
      />
      <div class="section-container">
        <CheckBox
          disabled={false}
          checked={remember}
          checkboxName="Remember Me"
          on:change={handleChange}
        />
        <Link to="/auth/reset"><span>forgot password?</span></Link>
      </div>
      <Button hoverized={true} disabled={!disabled}
        >{!disabled ? `Please Login again in ${$loginTimer}s` : "Login"}</Button
      >

      <p class="verification-resend">
        <!-- svelte-ignore a11y-click-events-have-key-events -->
        <!-- svelte-ignore a11y-no-static-element-interactions -->
        Didn't Receive the Verification?
        <span class:t={setStylesDisabled} on:click={handleResend}
          >{!disabledResend ? `Resend in ${$resendTimer}s` : "Resend"}</span
        >
      </p>
    </form>
  </div>
</main>

<style>
  main {
    display: flex;
    align-items: center;
    justify-content: center;
    column-gap: 0.5rem;
    margin: 0 1.5rem;
    height: 90vh;

    & div.form-container {
      padding: 1.5rem;
      max-width: 27rem;
      width: 100%;
      border-radius: 2rem;
      box-shadow: 2px 3px 5px rgba(0, 0, 0, 0.1);

      & form.form {
        text-align: center;

        & img.favicon-elegant {
          max-width: 5rem;
        }

        & div.title-container {
          margin-bottom: 2rem;

          & h1 {
            font-size: 2.5rem;
            font-weight: bold;
            letter-spacing: -0.12rem;
            color: var(--main-col-3);
          }

          & p {
            color: var(--scroll-color);

            & span {
              text-decoration: none;
              color: var(--border-hover-color);
              transition: all ease-in-out 200ms;
            }

            & span:hover {
              opacity: 0.6;
              text-decoration: underline;
            }
          }
        }
      }

      & div.section-container {
        display: flex;
        justify-content: space-between;
        margin: 1.7rem 0;

        & span {
          text-decoration: none;
          color: var(--border-hover-color);
          transition: all ease-in-out 200ms;
        }

        & span:hover {
          opacity: 0.6;
          text-decoration: underline;
        }
      }

      & p.verification-resend {
        margin-top: 1rem;
        color: var(--scroll-color);

        & span {
          text-decoration: none;
          color: var(--border-hover-color);
          transition: all ease-in-out 200ms;
          cursor: pointer;
        }

        & span:hover {
          opacity: 0.6;
          text-decoration: underline;
        }

        & span.t {
          opacity: 0.6;
          pointer-events: none;
        }
      }
    }
  }

  @media (max-height: 600px) {
    main {
      margin: 8rem 0;
    }
  }

  @media (max-width: 350px) {
    main form div.section-container {
      flex-direction: column;
      align-items: center;
      row-gap: 1rem;
    }
  }
</style>
