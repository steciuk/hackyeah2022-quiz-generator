export class GenerateRequestDTO {
  constructor(
    public readonly sourceUrl: string,
    public readonly title: string,
    public readonly num_pages: number
  ) {}
}
