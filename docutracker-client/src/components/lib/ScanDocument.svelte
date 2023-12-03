<script lang="ts">
  import { Html5Qrcode } from "html5-qrcode";
  import { dark, handleFetch, address, type RequestAPI } from "../../store";
  import { onMount } from "svelte";

  import WebcamIcon from "../icons/WebcamIcon.svelte";
  import FileSystemIcon from "../icons/FileSystemIcon.svelte";
  import Button from "../shared/Button.svelte";
  import Cropper from "svelte-easy-crop";
  import jsQR from "jsqr";

  export let authToken = "";

  let scanning = false;
  let html5Qrcode: Html5Qrcode;
  let fileData: FileList;
  let base64String: string | null;
  let pixelCrop: { width: number; height: number; x: number; y: number };
  let fileName = "Upload Your Profile";
  let croppedImage: string | null;
  let crop: { x: number; y: number };
  let zoom = 1;

  function handleImage() {
    croppedImage = null;
    zoom = 1;
    crop = { x: 0, y: 0 };

    let files = fileData[0];
    fileName = files.name;
    const reader = new FileReader();

    reader.onload = function (e) {
      if (typeof e.target!.result === "string") {
        base64String = e.target!.result;
      } else {
        console.warn("Event target is an Array Buffer at line 33");
      }
    };

    reader.readAsDataURL(files);
  }

  const createImage = (url: string) =>
    new Promise((resolve, reject) => {
      const image = new Image();
      image.addEventListener("load", () => resolve(image));
      image.addEventListener("error", (error) => reject(error));
      image.setAttribute("crossOrigin", "anonymous");
      image.src = url;
    });

  function getRadianAngle(degreeValue: number) {
    return (degreeValue * Math.PI) / 180;
  }

  export async function getCroppedImg(
    imageSrc: string | null,
    pixelCrop: { width: any; height: any; x: any; y: any },
    rotation = 0
  ): Promise<string> {
    const image = (await createImage(imageSrc!)) as HTMLImageElement;
    const canvas: HTMLCanvasElement = document.createElement("canvas");
    const ctx: CanvasRenderingContext2D = canvas.getContext("2d")!;

    const maxSize = Math.max(image.width, image.height);
    const safeArea = 2 * ((maxSize / 2) * Math.sqrt(2));

    canvas.width = safeArea;
    canvas.height = safeArea;

    ctx.translate(safeArea / 2, safeArea / 2);
    ctx.rotate(getRadianAngle(rotation));
    ctx.translate(-safeArea / 2, -safeArea / 2);

    ctx.drawImage(
      image,
      safeArea / 2 - image.width * 0.5,
      safeArea / 2 - image.height * 0.5
    );
    const data = ctx.getImageData(0, 0, safeArea, safeArea);

    canvas.width = pixelCrop.width;
    canvas.height = pixelCrop.height;

    ctx.putImageData(
      data,
      Math.round(0 - safeArea / 2 + image.width * 0.5 - pixelCrop.x),
      Math.round(0 - safeArea / 2 + image.height * 0.5 - pixelCrop.y)
    );

    return new Promise((resolve) => {
      canvas.toBlob((file) => {
        resolve(URL.createObjectURL(file!));
      }, "image/png");
    });
  }

  export async function getRotatedImage(imageSrc: string, rotation = 0) {
    const image = (await createImage(imageSrc)) as HTMLImageElement;
    const canvas: HTMLCanvasElement = document.createElement("canvas");
    const ctx: CanvasRenderingContext2D = canvas.getContext("2d")!;

    const orientationChanged =
      rotation === 90 ||
      rotation === -90 ||
      rotation === 270 ||
      rotation === -270;
    if (orientationChanged) {
      canvas.width = image.height;
      canvas.height = image.width;
    } else {
      canvas.width = image.width;
      canvas.height = image.height;
    }

    ctx.translate(canvas.width / 2, canvas.height / 2);
    ctx.rotate((rotation * Math.PI) / 180);
    ctx.drawImage(image, -image.width / 2, -image.height / 2);

    return new Promise((resolve) => {
      canvas.toBlob((file) => {
        resolve(URL.createObjectURL(file!));
      }, "image/webp");
    });
  }

  const scanMethod = "POST";
  const scanAddress = `${address}/scan`;
  const scanRequest: RequestAPI = {
    method: scanMethod,
    address: scanAddress,
    credentials: { codeData: "" },
  };

  onMount(() => {
    html5Qrcode = new Html5Qrcode("reader");
  });

  function scan() {
    scanning = true;

    html5Qrcode.start(
      { facingMode: "environment" },
      {
        fps: 10,
        qrbox: { width: 200, height: 200 },
      },
      onScanSuccess,
      onScanFailure
    );
  }

  async function stop() {
    scanning = false;
    await html5Qrcode.stop();
  }

  async function onScanSuccess(
    decodedText: string,
    decodedResult: { decodedText: string; result: { text: string } }
  ) {
    scanRequest.credentials!.codeData = decodedText;
    const request = await handleFetch(scanRequest, authToken);
    console.log(request);
  }

  function onScanFailure(error: any) {
    console.warn(`Code scan error = ${error}`);
  }

  let img = new Image();

  const handleFileSystemScan = async () => {
    if (
      base64String !== null &&
      base64String !== undefined &&
      base64String.length
    ) {
      img.src = base64String;

      img.onload = async function () {
        let canvas = document.createElement("canvas");
        canvas.width = img.width;
        canvas.height = img.height;
        let context = canvas.getContext("2d");
        context!.drawImage(img, 0, 0, img.width, img.height);
        let imageData = context!.getImageData(0, 0, img.width, img.height);
        let decodedQR = jsQR(imageData.data, img.width, img.height);

        if (decodedQR) {
          scanRequest.credentials!.codeData = decodedQR.data;
          const request = await handleFetch(scanRequest, authToken);
          console.log(request);
        } else {
          console.log("No QR code found in image.");
        }
      };
    }

    console.warn("No Image Uploaded.");
  };
</script>

<div class="qr-wrapper">
  <div class="scan" class:dark={$dark}>
    <div class="title-container">
      <WebcamIcon></WebcamIcon>
      <span class="title" class:dark={$dark}> Webcam </span>
    </div>
    <div
      class="scan-wrapper"
      class:is-scanning={scanning}
      class:dark={$dark}
      id="reader"
    >
      {#if !scanning}
        <span class="scan-body"> Make sure you allow Camera access! </span>
      {/if}
    </div>
    {#if scanning}
      <Button on:click={stop}>stop</Button>
    {:else}
      <Button on:click={scan}>start</Button>
    {/if}
  </div>
  <div class="scan" class:dark={$dark}>
    <div class="title-container">
      <FileSystemIcon></FileSystemIcon>
      <span class="title" class:dark={$dark}> File System </span>
    </div>
    <div class="scan-wrapper file-system" class:dark={$dark}>
      <input
        id="scan-input"
        bind:files={fileData}
        on:change={handleImage}
        type="file"
        accept=".jpg, .jpeg, .png"
      />

      {#if base64String}
        <!-- svelte-ignore a11y-img-redundant-alt -->
        <Cropper
          image={base64String}
          bind:crop
          bind:zoom
          aspect={1}
          on:cropcomplete={(e) => (pixelCrop = e.detail.pixels)}
        />
      {:else}
        <label class="scan-trigger" for="scan-input">
          <span class="scan-body"> Select an Image! </span>
        </label>
      {/if}
    </div>
    <Button on:click={handleFileSystemScan}>Scan</Button>
  </div>
</div>

<style>
  div.qr-wrapper {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    justify-content: center;
    column-gap: 3rem;
    height: 100%;

    & div.scan {
      transition: all ease-in-out 300ms;
      border: 1px solid var(--header-color);
      padding: 1rem;
      color: var(--scroll-color);

      & div.title-container {
        display: flex;
        align-items: center;
        column-gap: 0.5rem;
        margin-bottom: 1rem;

        & span.title {
          transition: color ease-in-out 300ms;
          font-size: 1rem;
          display: inline-block;
          font-weight: bold;
        }

        & span.dark {
          color: var(--background);
        }
      }

      & div.scan-wrapper {
        position: relative;
        transition: all ease-in-out 300ms;
        overflow: hidden;
        display: flex;
        justify-content: center;
        align-items: center;
        margin-bottom: 2rem;
        width: 32rem;
        height: 24rem;
        background-color: var(--main-col-1);

        & input[type="file"] {
          display: none;
        }

        & label.scan-trigger {
          cursor: pointer;
          display: block;
          width: 100%;
          height: 100%;
          display: flex;
          align-items: center;
          justify-content: center;
        }

        & span.scan-body {
          color: var(--background);
        }
      }

      & div.scan-wrapper.file-system {
        display: block;
      }

      & div.dark {
        background-color: var(--dark-main-col-1);
      }

      & div.is-scanning {
        border-color: transparent;
      }
    }

    & div.scan.dark {
      border-color: var(--input-color);
    }

    & div.filesystem {
      width: 30rem;
      height: 25rem;
      background-color: red;
    }
  }

  @media (max-width: 800px) {
    div.qr-wrapper div.scan div.scan-wrapper {
      width: 27rem;
      height: 25rem;
    }
  }

  @media (max-width: 650px) {
    div.qr-wrapper div.scan div.scan-wrapper {
      width: 22rem;
      height: 17rem;
    }
  }
</style>
