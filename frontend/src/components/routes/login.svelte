<script>
  // @ts-nocheck

  import { Link, navigate } from "svelte-routing";
  import { onMount, onDestroy } from "svelte";
  import {
    pageTransitionValue1,
    pageTransitionValue2,
    loaderState,
    serverResponse,
    backendAddress,
    fetchData,
  } from "../../stores";

  import Input from "../entries/input.svelte";
  import Form from "../entries/form.svelte";
  import BarLoader from "../assets/barLoader.svelte";
  import Button from "../entries/button.svelte";
  import favicon from "../../lib/transparent-favicon-elegant.png";
  import Checkbox from "../entries/checkbox.svelte";
  import Auth from "../entries/auth.svelte";

  let email = "";
  let password = "";
  let userEmail = localStorage.getItem("userEmail") || "";
  let disableResend = false;
  let timeLeft = 0;
  let checkboxValue = false;
  // let authBind;

  const method = "POST";
  const errorMessage = "Server is down, please try again later.";
  const body = JSON.stringify({ userEmail: userEmail });
  const api = `${backendAddress}login`;
  const resendAPI = `${backendAddress}resend`;
  const confirmation = `${backendAddress}confirmed_check`;
  const navigateUser = "/home";

  const storedResendTime = localStorage.getItem("resendTime");
  if (storedResendTime) {
    const elapsedTime = Date.now() - storedResendTime;
    const delay = 60000;

    if (elapsedTime < delay) {
      disableResend = true;
      timeLeft = Math.ceil((delay - elapsedTime) / 1000);

      const countdown = setInterval(() => {
        if (timeLeft > 0) {
          timeLeft -= 1;
        } else {
          clearInterval(countdown);
          disableResend = false;
        }
      }, 1000);
    }
  }

  const handleReset = (e) => {
    email = e.detail;
    password = e.detail;
  };

  const handlecheckChange = () => {
    if (email.trim().length === 0 || password.trim().length === 0) {
      $serverResponse = { error: "Please fill all Entries first!" };
      checkboxValue = false;
      return;
    }

    checkboxValue = !checkboxValue;
  };

  $: if (email.trim().length === 0 || password.trim().length === 0) {
    checkboxValue = false;

    if (!checkboxValue) {
      sessionStorage.setItem("email", undefined);
      sessionStorage.setItem("password", undefined);
    }
  }

  $: if (checkboxValue) {
    sessionStorage.setItem("email", email);
    sessionStorage.setItem("password", password);
  } else {
    sessionStorage.setItem("email", undefined);
    sessionStorage.setItem("password", undefined);
  }

  async function handleResend() {
    if (disableResend) return;

    if (userEmail.length === 0) {
      $serverResponse = {
        error: "Please Sign Up First!",
      };

      navigate("/auth/u/signup");
      return;
    }

    disableResend = true;

    try {
      const sendEmail = await fetch(resendAPI, {
        method: method,
        headers: {
          "Content-Type": "application/json",
        },
        body: body,
      });

      if (sendEmail.ok) {
        $serverResponse = await sendEmail.json();
        if ($serverResponse.response) {
          localStorage.setItem("resendTime", Date.now());
          disableResend = true;
          timeLeft = 60;

          const countdown = setInterval(() => {
            if (timeLeft > 0) {
              timeLeft -= 1;
            } else {
              clearInterval(countdown);
              disableResend = false;
            }
          }, 1000);
        } else {
          disableResend = false;
        }
      }
    } catch {
      $serverResponse = {
        error: errorMessage,
      };

      disableResend = false;
    }
  }

  onMount(() => {
    document.body.className = "body-class";
    document.title = "DOCUTRACKER | Login";

    const axisValue = -150;
    const duration = 250;
    const delay = 350;

    $pageTransitionValue1 = {
      x: axisValue,
      duration: duration,
      delay: delay,
    };

    $pageTransitionValue2 = {
      x: axisValue + delay,
      duration: duration,
    };
    // authBind.postEndPoint(confirmation, errorMessage, body);
  });

  onDestroy(() => {
    document.body.className = "";
  });
</script>

<!-- <Auth bind:this={authBind} /> -->

{#if $loaderState}
  <BarLoader />
{/if}

<section>
  <img src={favicon} alt="Docutracker's Logo" />
  <header>
    <h1>Welcome back</h1>
    <p>
      Don't have an account?
      <Link to="/auth/u/signup"><span>Signup</span></Link>
    </p>
  </header>
  <Form {email} {password} {api} {navigateUser} on:resetInput={handleReset}>
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
      <Checkbox
        checkboxDisabled={false}
        checkboxName={"Remember Me"}
        checkboxChecked={checkboxValue}
        on:change={handlecheckChange}
      />
      <a href="/auth/u/reset"><span>forgot password?</span></a>
    </div>
    <Button btnName={"Login"} btnLoginSize={true} btnTitle={"Login"} />
    <!-- {#if !$fetchData.response} -->
    <p>
      <!-- svelte-ignore a11y-click-events-have-key-events -->
      <!-- svelte-ignore a11y-no-static-element-interactions -->
      Didn't Receive the Verification?
      <span on:click={handleResend} class:disabled={disableResend}
        >Resend {timeLeft ? `again in (${timeLeft}s)` : "Again"}</span
      >
    </p>
    <!-- {/if} -->
  </Form>
</section>

<style>
  section {
    border-radius: 1rem;
    padding: var(--size-3);
    box-shadow: 10px 10px 50px var(--main-col-2);

    display: flex;
    flex-direction: column;
    align-items: center;

    & img {
      max-width: var(--size-2);
    }

    & span {
      text-decoration: none;
      color: var(--brdr-hovr);
      transition: all ease-in-out 200ms;
      cursor: pointer;
    }

    & span:hover {
      opacity: var(--opacity);
      text-decoration: underline;
    }

    & span.disabled {
      pointer-events: none;
      opacity: 0.6;
    }

    & header {
      margin-bottom: 1rem;

      & p {
        margin: 1rem 0 2rem 0;

        & span {
          text-decoration: none;
          color: var(--brdr-hovr);
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
        color: var(--main-col-1);
      }

      & a:hover {
        text-decoration: underline;
      }
    }
  }
</style>
