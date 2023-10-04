<script>
  // @ts-nocheck

  import { backendAddress, loaderState } from "../../stores";
  import { onMount } from "svelte";
  import { Link } from "svelte-routing";

  import Form from "../entries/form.svelte";
  import Input from "../entries/input.svelte";
  import Button from "../entries/button.svelte";
  import BarLoader from "../assets/barLoader.svelte";
  import forgotPassword_banner from "../../lib/forgot-password-banner.png";

  let email = "";
  let api = `${backendAddress}reset`;
  let disableResend = false;
  let timeLeft = 0;

  const navigateUser = "/auth/u/login";
  const parentName = "reset";
  const warnMessage =
    "If you can't see your Email, try checking out Spam Messages!";

  const storedResendTime = localStorage.getItem("passwordResendTime");
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

  const handleResetPassword = () => {
    localStorage.setItem("passwordResendTime", Date.now());
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
  };

  onMount(() => {
    document.body.className = "body-class";
    document.title = "DOCUTRACKER | Forgot Password";
  });

  const handleResetEntry = (e) => {
    email = e.detail;
  };
</script>

{#if $loaderState}
  <BarLoader />
{/if}
<section>
  <img src={forgotPassword_banner} alt="Forgot Password Banner" />
  <div class="reset-entry-wrapper">
    <header>
      <h1>Forgot Password?</h1>
      <p>
        Please keep in mind that you only have 1 attemp to change your password
        every 7 days!
      </p>
    </header>
    <Form
      {email}
      {disableResend}
      {api}
      {warnMessage}
      {navigateUser}
      {handleResetPassword}
      {parentName}
      on:resetInput={handleResetEntry}
    >
      <Input
        inputName={"Your Existing Email"}
        inputType={"email"}
        inputAutocomplete={"on"}
        inputValue={email}
        on:input={(e) => (email = e.target.value)}
      />

      <Button
        btnName={disableResend
          ? `Resend again in (${timeLeft}s)`
          : "Forgot Password"}
        btnTitle={"Forgot Password"}
        btnLoginSize={true}
        btnDisabled={disableResend}
      />
      <p>
        Go back to <Link to="/auth/u/login"><span>Login</span></Link>
      </p>
    </Form>
  </div>
</section>

<style>
  section {
    display: flex;
    justify-content: center;
    align-items: center;
    column-gap: var(--size-3);

    & img {
      max-width: calc(var(--size-4) * 0.5);
    }

    & div.reset-entry-wrapper {
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: flex-start;
      row-gap: var(--size-1);

      & header {
        display: flex;
        justify-content: center;
        flex-direction: column;
        row-gap: calc(var(--size-5) * 0.5);
        max-width: var(--size-4);

        & h1 {
          font-family: Arial;
          font-size: 2rem;
          font-weight: bold;
          letter-spacing: -0.12rem;
        }

        & p {
          color: var(--for-col);
        }
      }
    }

    & p {
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
  }
</style>
