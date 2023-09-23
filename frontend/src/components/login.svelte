<script>
  // @ts-nocheck

  import { Link, navigate } from "svelte-routing";
  import { onMount, onDestroy } from "svelte";
  import {
    pageTransitionValue1,
    pageTransitionValue2,
    loaderState,
    serverResponse,
  } from "../stores";

  import Input from "./entries/input.svelte";
  import Form from "./entries/form.svelte";
  import BarLoader from "./assets/barLoader.svelte";

  let email = "";
  let password = "";
  // let navigateUser = "";
  
  const api = "http://127.0.0.1:5000/login";
  const resendAPI = "http://127.0.0.1:5000/resend";
  const confirmation = "http://127.0.0.1:5000/email_confirmation";

  const handleReset = (e) => {
    email = e.detail;
    password = e.detail;
  };

  async function handleResend() {
    let userEmail = localStorage.getItem("userEmail") || "";

    if (userEmail.length === 0) {
      $serverResponse = {
        error: "Please Sign Up First!",
      };
      navigate("/signup");
      return;
    }

    try {
      const sendEmail = await fetch(resendAPI, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ userEmail: userEmail }),
      });

      if (sendEmail.ok) {
        $serverResponse = await sendEmail.json();
      }
    } catch {
      $serverResponse = {
        error: "Server is down, please try again later.",
      };
    }
  }

  onMount(() => {
    document.body.className = "body-class";
    document.title = "Docutracker | Login";
    $pageTransitionValue1 = -150;
    $pageTransitionValue2 = 150;

    const userEmail = localStorage.getItem("userEmail");
    if (userEmail || userEmail.length !== 0 || userEmail !== undefined) {
      fetch(confirmation, {
        method: "POST",
        headers: {
          Authorization: `Bearer ${userEmail}`,
        },
      }).then((response) => console.log(response));
    }
  });

  onDestroy(() => {
    document.body.className = "";
  });
</script>

{#if $loaderState}
  <BarLoader />
{/if}

<section>
  <header>
    <h1>Welcome back</h1>
    <p>
      Don't have an account?
      <Link to="/signup"><span>Signup</span></Link>
    </p>
  </header>
  <Form {email} {password} {api} on:resetInput={handleReset}>
    <Input
      inputName={"Email"}
      inputType={"email"}
      inputAutocomplete={"on"}
      inputValue={email}
      on:input={(e) => (email = e.target.value)}
    />
    <Input
      inputName={"Password"}
      inputType={"password"}
      inputAutocomplete={"off"}
      inputValue={password}
      on:input={(e) => (password = e.target.value)}
    />
    <div class="container">
      <div class="checkbox">
        <input id="remember" type="checkbox" />
        <label class="remmember" for="remember">Remember me</label>
      </div>
      <a href="/Authentication/ResetPassword">forgot password?</a>
    </div>
    <button>Login</button>
    <p>
      <!-- svelte-ignore a11y-click-events-have-key-events -->
      <!-- svelte-ignore a11y-no-static-element-interactions -->
      Didn't Receive the Verification?
      <span on:click={handleResend}>Resend</span>
    </p>
  </Form>
</section>

<style>
  section {
    border-radius: 1rem;
    padding: 3rem;
    box-shadow: 10px 10px 50px lightgray;

    & span {
      text-decoration: none;
      color: orange;
      transition: all ease-in-out 200ms;
      cursor: pointer;
    }

    & span:hover {
      opacity: var(--opacity);
      text-decoration: underline;
    }

    & header {
      margin-bottom: 1rem;

      & p {
        margin: 1rem 0 2rem 0;

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

      & h1 {
        font-family: Arial;
        font-size: 2rem;
        font-weight: bold;
        letter-spacing: -0.12rem;
      }
    }

    & div.container {
      display: flex;
      justify-content: space-between;
      width: 100%;
      margin: 0.5rem 0;

      & div.checkbox,
      input,
      label.remmember {
        cursor: pointer;
        color: gray;
      }

      & a:hover {
        text-decoration: underline;
      }
    }

    & button {
      width: 100%;
      height: 2rem;
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
  }
</style>
