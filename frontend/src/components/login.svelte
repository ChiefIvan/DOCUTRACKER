<script>
  // @ts-nocheck

  import { Link } from "svelte-routing";
  import { onMount, onDestroy } from "svelte";
  import { pageTransitionValue1, pageTransitionValue2 } from "../stores";

  import Input from "./entries/input.svelte";
  import Form from "./entries/form.svelte";

  let email = "";
  let password = "";
  let api = "http://127.0.0.1:5000/login";

  const handleReset = (e) => {
    email = e.detail;
    password = e.detail;
  };

  onMount(() => {
    document.body.className = "body-class";
    document.title = "Docutracker | Login";
  });

  onDestroy(() => {
    document.body.className = "";
  });

  const handleTransition = () => {
    $pageTransitionValue1 = -150;
    $pageTransitionValue2 = 150;
  };
</script>

<section>
  <header>
    <h1>Wecome back</h1>
    <p>
      Don't have an account?
      <!-- svelte-ignore a11y-click-events-have-key-events -->
      <!-- svelte-ignore a11y-no-static-element-interactions -->
      <Link to="/signup"><span on:click={handleTransition}>Signup</span></Link>
    </p>
  </header>
  <Form {email} {password} {api} on:resetInput={handleReset}>
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
      miniModal={"Your password must be greater than 7 characters and have atleat 1 Uppercase, 1 lowercase and a number!"}
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
  </Form>
</section>

<style>
  section {
    border-radius: 1rem;
    padding: 4rem;
    box-shadow: 10px 10px 50px lightgray;

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
      }

      & a:hover {
        text-decoration: underline;
      }
    }

    & button {
      width: 100%;
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
  }
</style>
