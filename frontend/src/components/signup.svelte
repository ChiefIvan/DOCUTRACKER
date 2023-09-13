<script>
  // @ts-nocheck
  import { Link } from "svelte-routing";
  import { onMount, onDestroy } from "svelte";
  import {
    pageTransitionValue1,
    pageTransitionValue2,
    loaderState,
  } from "../stores";

  import Input from "./entries/input.svelte";
  import Form from "./entries/form.svelte";
  import banner from "../lib/signup_banner.png";
  import BarLoader from "./assets/barLoader.svelte";

  let userName = "";
  let email = "";
  let password = "";
  let cnfrmPassword = "";
  let passwordErroColor = "";
  let navigateUser = "/login";
  let api = "http://127.0.0.1:5000/signup";
  const passwordLabel =
    "Your password must be greater than 7 characters and have atleat 1 uppercase, 1 lowercase and a number!";

  onMount(() => {
    document.body.className = "body-class";
    document.title = "Docutracker | Signup";
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

  const handleTransition = () => {
    $pageTransitionValue1 = 150;
    $pageTransitionValue2 = -150;
  };

  $: {
    if (cnfrmPassword.length != 0) {
      if (password !== cnfrmPassword) {
        passwordErroColor = "crimson";
      } else {
        passwordErroColor = "";
      }
    }
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
      miniModal={"Your Username must be greater than 3 charecters"}
      on:input={(e) => (userName = e.target.value)}
    />
    <Input
      inputName={"Email"}
      inputType={"email"}
      inputAutocomplete={"on"}
      inputValue={email}
      miniModal={"Please include the @ symbol!"}
      on:input={(e) => (email = e.target.value)}
    />
    <Input
      inputName={"Password"}
      inputType={"password"}
      inputAutocomplete={"off"}
      inputValue={password}
      miniModal={passwordLabel}
      errorColor={passwordErroColor}
      on:input={(e) => (password = e.target.value)}
    />
    <Input
      inputName={"Confirm Password"}
      inputType={"password"}
      inputAutocomplete={"off"}
      inputValue={cnfrmPassword}
      miniModal={passwordLabel}
      errorColor={passwordErroColor}
      on:input={(e) => (cnfrmPassword = e.target.value)}
    />
    <div class="container">
      <div class="checkbox">
        <input id="remember" type="checkbox" />
        <label class="remmember" for="remember">Remember me</label>
      </div>
      <a href="/Authentication/ResetPassword">forgot password?</a>
    </div>
    <button>Submit</button>
    <p>
      <!-- svelte-ignore a11y-click-events-have-key-events -->
      <!-- svelte-ignore a11y-no-static-element-interactions -->
      Already have an account? <Link to="/login"
        ><span on:click={handleTransition}>Login</span></Link
      >
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
  }

  section {
    display: flex;
    justify-content: center;
    align-items: center;
    column-gap: 5rem;

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

      & div.checkbox,
      input,
      label.remmember {
        cursor: pointer;
      }

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
