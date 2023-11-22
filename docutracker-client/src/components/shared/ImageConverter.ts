export async function blobToBase64(blobUrl: string | null) {
  if (blobUrl === null) {
    throw new Error("blobUrl cannot be null");
  }

  const response = await fetch(blobUrl);
  const blob = await response.blob();

  return new Promise<string>((resolve, reject) => {
    const reader = new FileReader();
    reader.onloadend = () => resolve(reader.result as string);
    reader.onerror = reject;
    reader.readAsDataURL(blob);
  });
}
