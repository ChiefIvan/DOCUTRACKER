<script>
  // @ts-nocheck
  import { Link } from "svelte-routing";
  import { onMount, onDestroy } from "svelte";
  import {
    pageTransitionValue1,
    pageTransitionValue2,
    loaderState,
    captchaVerification,
  } from "../stores";

  import Input from "./entries/input.svelte";
  import Form from "./entries/form.svelte";
  import banner from "../lib/signup_banner.png";
  import BarLoader from "./assets/barLoader.svelte";
  import CaptchaCheckbox from "./entries/captcha.svelte";

  let userName = "";
  let email = "";
  let password = "";
  let cnfrmPassword = "";
  let passwordErrorColor = "";

  let buttonDisabled = true;
  let captchaDisabled = true;
  let navigateUser = "/login";
  let api = "http://127.0.0.1:5000/signup";
  const passwordLabel =
    "Your password must be greater than 7 characters and have atleat 1 uppercase, 1 lowercase and a number!";

  onMount(() => {
    document.body.className = "body-class";
    document.title = "Docutracker | Signup";
    $pageTransitionValue1 = 150;
    $pageTransitionValue2 = -150;
    $captchaVerification = false;
  });

  onDestroy(() => {
    document.body.className = "";
  });

  const handleReset = (e) => {
    userName = e.detail;
    email = e.detail;
    password = e.detail;
    cnfrmPassword = e.detail;
  };

  const handleTransition = (e) => {
    console.log(e.target.innerText);
  };

  $: {
    passwordErrorColor =
      cnfrmPassword.length && password !== cnfrmPassword ? "crimson" : "";
    captchaDisabled = [userName, email, password, cnfrmPassword].some(
      (value) => value.length === 0
    );
    buttonDisabled = !$captchaVerification && true;
  }
</script>

{#if $loaderState}
  <BarLoader />
{/if}

<section>
  <img src={banner} alt="login banner" />
  <Form
    {userName}
    {email}
    {password}
    {cnfrmPassword}
    {api}
    {navigateUser}
    on:resetInput={handleReset}
  >
    <header>
      <h1>Sign up</h1>
    </header>
    <Input
      inputName={"Username"}
      inputType={"text"}
      inputAutocomplete={"off"}
      inputValue={userName}
      miniModal={"Your Username must be greater than 3 charecters!"}
      on:input={(e) => (userName = e.target.value)}
    />
    <Input
      inputName={"Email"}
      inputType={"email"}
      inputAutocomplete={"on"}
      inputValue={email}
      miniModal={"Your email name must be greater than 3 characters, before the @ symbol!"}
      on:input={(e) => (email = e.target.value)}
    />
    <Input
      inputName={"Password"}
      inputType={"password"}
      inputAutocomplete={"off"}
      inputValue={password}
      miniModal={passwordLabel}
      errorColor={passwordErrorColor}
      on:input={(e) => (password = e.target.value)}
    />
    <Input
      inputName={"Confirm Password"}
      inputType={"password"}
      inputAutocomplete={"off"}
      inputValue={cnfrmPassword}
      miniModal={passwordLabel}
      errorColor={passwordErrorColor}
      on:input={(e) => (cnfrmPassword = e.target.value)}
    />
    <div class="container">
      <div>
        <CaptchaCheckbox checkboxDisabled={captchaDisabled} />
      </div>
      <a href="/Authentication/ResetPassword">forgot password?</a>
    </div>
    <button
      title={buttonDisabled ? "Please fill all entries first" : ""}
      class:btn-disabled={buttonDisabled}
      disabled={buttonDisabled}>Submit</button
    >
    <p>
      Already have an account? <Link to="/login"><span>Login</span></Link>
    </p>
  </Form>
</section>

<style>
  :root {
    --opacity: 0.6;
  }

  :global(.body-class) {
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    overflow: hidden;
  }

  section {
    display: flex;
    justify-content: center;
    align-items: center;
    column-gap: 2rem;

    & img {
      max-width: 30rem;
    }

    & header {
      margin-bottom: 2rem;

      & h1 {
        font-family: Arial;
        font-size: 2.5rem;
        font-weight: bold;
        letter-spacing: -0.12rem;
      }
    }

    & div.container {
      display: flex;
      justify-content: space-between;
      width: 100%;
      margin: 1.2rem 0;

      & a:hover {
        text-decoration: underline;
      }
    }

    & button {
      width: 8rem;
      height: 2.5rem;
      border: none;
      color: white;
      background-color: orange;
      cursor: pointer;
      border-radius: 5px;
      transition: all ease-in-out 300ms;
    }

    & button:hover {
      opacity: var(--opacity);
      box-shadow: 5px 5px 25px gray;
    }

    & .btn-disabled {
      background-color: gray;
    }

    & .btn-disabled:hover {
      box-shadow: none;
      opacity: 1;
      cursor: not-allowed;
    }

    & p {
      & span {
        text-decoration: none;
        color: orange;
        transition: all ease-in-out 200ms;
      }

      & span:hover {
        opacity: var(--opacity);
        text-decoration: underline;
      }
    }
  }
</style>
