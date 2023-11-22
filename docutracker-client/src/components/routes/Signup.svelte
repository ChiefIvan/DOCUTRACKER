<script lang="ts">
  import { Link, navigate } from "svelte-routing";
  import {
    type RequestAPI,
    type ResponseData,
    type SignUpBind,
    type Credentials,
    handleFetch,
    address,
    showMessage,
  } from "../../store";

  import signUpBanner from "./../../assets/signup_banner.png";
  import logoElegant from "./../../assets/transparent-favicon-elegant.png";
  import Input from "../shared/Input.svelte";
  import Button from "../shared/Button.svelte";
  import MediaQuery from "./../shared/MediaQuery.svelte";
  import CheckBox from "../shared/CheckBox.svelte";
  import Captcha from "../lib/Captcha.svelte";
  import BarLoader from "../shared/BarLoader.svelte";

  let bindForm: HTMLFormElement;
  let checkValue = false;
  let isRequest = false;

  let allVerified = false;
  let userNameVerified = true;
  let emailVerified = true;
  let passwordVerified = true;
  let cnfrmPasswordVerified = true;
  let emailPattern = new RegExp(
    "^[a-zA-Z0-9._%+-]{5,}@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$"
  );
  let passwordPattern = new RegExp("^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).*$");

  let newUser: Credentials = {
    userName: "",
    email: "",
    password: "",
    cnfrmPassword: "",
    captVerification: false,
  };

  $: newUser.userName && newUser.userName.length && newUser.userName.length < 4
    ? (userNameVerified = false)
    : (userNameVerified = true);

  $: newUser.email && newUser.email.length && !emailPattern.test(newUser.email)
    ? (emailVerified = false)
    : (emailVerified = true);

  $: (newUser.password &&
    newUser.password.length &&
    newUser.password.length < 8) ||
  (newUser.password &&
    newUser.password.length &&
    !passwordPattern.test(newUser.password))
    ? (passwordVerified = false)
    : (passwordVerified = true);

  $: newUser.cnfrmPassword &&
  newUser.cnfrmPassword.length &&
  newUser.password !== newUser.cnfrmPassword
    ? (cnfrmPasswordVerified = false)
    : (cnfrmPasswordVerified = true);

  $: if (
    newUser.userName &&
    newUser.userName.length &&
    newUser.email &&
    newUser.email.length &&
    newUser.password &&
    newUser.password.length &&
    newUser.cnfrmPassword &&
    newUser.cnfrmPassword.length
  ) {
    allVerified =
      userNameVerified &&
      emailVerified &&
      passwordVerified &&
      cnfrmPasswordVerified;
  }

  let inputBinds: SignUpBind = {
    userNameInput: false,
    emailInput: false,
    passwordInput: false,
    cnfrmPasswordInput: false,
  };

  const handleInput = (event: Event) => {
    const target = event.target as HTMLInputElement;
    const id = target.id;

    if (id === "Username") {
      newUser.userName = target.value;
    }

    if (id === "Email") {
      newUser.email = target.value;
    }

    if (id === "Password") {
      newUser.password = target.value;
    }

    if (id === "Confirm Password") {
      newUser.cnfrmPassword = target.value;
    }
  };

  const signUpAddress = `${address}/signup`;
  const signUpMethod = "POST";
  let timeOutID: number | undefined;

  $: signUpRequest = {
    method: signUpMethod,
    address: signUpAddress,
    credentials: newUser,
  };

  const handleSubmit = async () => {
    isRequest = true;
    clearTimeout(timeOutID);

    try {
      const response: ResponseData = await handleFetch(signUpRequest);

      localStorage.setItem("email", newUser.email!);

      bindForm.reset();

      checkValue = false;
      allVerified = false;

      newUser = {
        userName: "",
        email: "",
        password: "",
        cnfrmPassword: "",
        captVerification: false,
      };

      inputBinds = {
        userNameInput: false,
        emailInput: false,
        passwordInput: false,
        cnfrmPasswordInput: false,
      };

      $showMessage = response;

      if (response.success) {
        navigate("/auth/login");
        timeOutID = setTimeout(() => {
          alert("If you can't see your Email, try checking out Spam Messages!");
        }, 1000);
      }
    } catch (error) {
      console.error(error);
      isRequest = false;
    }

    isRequest = false;
  };

  const captchaAddress = `${address}/captcha`;
  const captchaMethod = "GET";

  const captchaRequest: RequestAPI = {
    method: captchaMethod,
    address: captchaAddress,
  };

  let captchaImage = "";

  const handleCaptcha = async () => {
    try {
      const response: ResponseData = await handleFetch(captchaRequest);

      if (!response.captchaGETValue) {
        console.error("Captcha GET Values are undefined");
        return;
      }

      captchaImage = response.captchaGETValue[0];
      sessionStorage.setItem("captchaID", response.captchaGETValue[1]);
    } catch (error) {
      console.error(error);
    }
  };

  let attemps = 3;

  const handleDispatch = (event: { detail: boolean }) => {
    checkValue = event.detail;
    newUser.captVerification = checkValue;

    console.log(checkValue);

    if (!checkValue) {
      attemps--;

      if (attemps <= 0) {
        attemps = 3;
        console.warn("Captcha Verification failed!, please try again.");
        $showMessage = {
          error: "Captcha Verification failed!, please try again.",
        };
        captchaImage = "";

        return;
      }

      handleCaptcha();

      return;
    }

    attemps = 3;
    captchaImage = "";
  };
</script>

<svelte:head>
  <title>DOCUTRACKER | Signup</title>
</svelte:head>

{#if isRequest}
  <BarLoader />
{/if}

<main>
  <MediaQuery query="(min-width: 700px)" let:matches>
    {#if matches}
      <img class="signup-banner" src={signUpBanner} alt="Sign Up Banner" />
    {/if}
  </MediaQuery>

  {#if captchaImage.length !== 0}
    <Captcha {captchaImage} on:dispatch={handleDispatch} />
  {/if}

  <form
    bind:this={bindForm}
    on:submit|preventDefault={handleSubmit}
    autocomplete="off"
  >
    <MediaQuery query="(max-width: 700px)" let:matches>
      {#if matches}
        <img
          class="favicon-elegant"
          src={logoElegant}
          alt="Docutracker's Logo"
        />
      {/if}
    </MediaQuery>
    <h1>Sign up</h1>
    <Input
      inputType="text"
      inputName="Username"
      verifiedEntry={userNameVerified}
      tooltipContent="Your Username must be greater than 3 characters!"
      on:input={handleInput}
      bind:focusedInput={inputBinds.userNameInput}
    />
    <Input
      inputType="email"
      inputName="Email"
      verifiedEntry={emailVerified}
      tooltipContent="Your Email must have more than 4 characters before the '@', and both '@' symbol and a top-level domain are mandatory!"
      on:input={handleInput}
      bind:focusedInput={inputBinds.emailInput}
    />
    <Input
      inputType="password"
      inputName="Password"
      verifiedEntry={passwordVerified}
      tooltipContent="Your Password must be greater than 7 characters and have atleat 1 uppercase, 1 lowercase and a number!"
      on:input={handleInput}
      bind:focusedInput={inputBinds.passwordInput}
    />
    <Input
      inputType="password"
      inputName="Confirm Password"
      verifiedEntry={cnfrmPasswordVerified}
      tooltipContent="Your Password and Password Confirmation must be the same!"
      on:input={handleInput}
      bind:focusedInput={inputBinds.cnfrmPasswordInput}
    />
    <div class="section-container">
      <CheckBox
        disabled={checkValue ? true : !allVerified}
        checked={checkValue}
        checkboxName="I am not a robot"
        on:change={handleCaptcha}
      />
      <Link to="/auth/reset"><span>forgot password?</span></Link>
    </div>
    <div class="button-container">
      <div class="button">
        <Button hoverized={true} disabled={!checkValue}>Submit</Button>
      </div>
    </div>
    <p class="login-link">
      Already have an Account?
      <Link to="/auth/login">
        <span>Login</span>
      </Link>
    </p>
  </form>
</main>

<style>
  main {
    display: flex;
    align-items: center;
    justify-content: center;
    column-gap: 0.5rem;
    margin: 0 3rem;
    height: 90vh;

    & img.signup-banner {
      max-width: 25rem;
    }

    & form {
      max-width: 25rem;
      width: 100%;

      & img.favicon-elegant {
        max-width: 5rem;
      }

      & h1 {
        font-size: 2.5rem;
        font-weight: bold;
        letter-spacing: -0.12rem;
        color: var(--main-col-3);
        margin-bottom: 2rem;
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

      & div.button-container {
        display: flex;

        & div.button {
          width: 8rem;
        }
      }

      & p.login-link {
        margin: 1rem 0;
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

  @media (max-width: 700px) {
    main {
      margin: 0 2rem;
    }

    main form {
      text-align: center;
    }

    main form div.button-container {
      justify-content: center;
    }
  }

  @media (max-height: 600px) {
    main {
      margin: 7rem 0;
      text-align: center;
    }

    img.signup-banner {
      display: none;
    }

    main form div.button-container {
      justify-content: center;
    }
  }

  @media (max-width: 300px) {
    main {
      margin: 0 1rem;
    }

    main form div.section-container {
      flex-direction: column;
      align-items: center;
      row-gap: 1rem;
    }
  }
</style>
